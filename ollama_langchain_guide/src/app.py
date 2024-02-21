import time

import streamlit as st
from langchain_community.llms import Ollama

st.set_page_config(
    page_title="Phi-2 Chatbot",
    page_icon="ollama_langchain_guide/src/phi.svg",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": "https://github.com/Cutwell/ollama_langchain_guide",
        "Report a bug": "https://github.com/Cutwell/ollama_langchain_guide/issues/new",
        "About": "Example chatbot app demonstrating Phi-2 Local LLM response streaming with LangChain and Ollama.",
    },
)


@st.cache_resource
def getSystemPrompt():
    with open("ollama_langchain_guide/src/systemprompt.txt", "r") as file:
        return file.read()


def chat(prompt: str):
    with current_chat_message:
        # Block input to prevent sending messages whilst AI is responding
        st.session_state.disabled = True

        # Add user message to chat history
        st.session_state.messages.append(("human", prompt))

        # Display user message in chat message container
        with st.chat_message(
            "human", avatar="https://api.dicebear.com/7.x/thumbs/svg?seed=Kitty"
        ):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("ai", avatar="ollama_langchain_guide/src/phi.svg"):
            # Get complete chat history, including latest question as last message
            history = "\n".join(
                [f"{role}: {msg}" for role, msg in st.session_state.messages]
            )

            query = f"{history}\nAI:"

            placeholder = st.empty()
            response = ""

            for tokens in st.session_state.llm.stream(query):
                response += tokens
                # write response with "▌" to indicate streaming.
                with placeholder:
                    st.markdown(response + "▌")

            # write response without "▌" to indicate completed message.
            with placeholder:
                st.markdown(response)

        # Log AI response to chat history
        st.session_state.messages.append(("ai", response))
        # Unblock chat input
        st.session_state.disabled = False

        st.rerun()


if __name__ == "__main__":
    if "messages" not in st.session_state:
        # Initialise chat history when session starts
        st.session_state.messages = [
            (
                "system",
                getSystemPrompt().format(current_date=time.strftime("%Y-%m-%d")),
            ),
        ]

    if "disabled" not in st.session_state:
        # `disable` flag to prevent user from sending messages whilst the AI is responding
        st.session_state.disabled = False

    if "llm" not in st.session_state:
        # Initialise the Phi-2 LLM
        # Use stopwords "Question:" and "User:" and "human:" to try and stop LLM from hallucinating user messages and responding to itself.
        st.session_state.llm = Ollama(
            model="phi", stop=["Question:", "User:", "human:"]
        )

    with st.sidebar:
        st.markdown("**Model Settings**:")

        llm_temperature = st.slider(
            label="LLM Temperature", min_value=0.0, max_value=1.0, value=0.0, step=0.01
        )

        update_button = st.button("Apply Changes")

        if update_button:
            st.session_state.llm = Ollama(
                model="phi",
                stop=["Question:", "User:", "human:"],
                temperature=llm_temperature,
            )

            st.toast(
                f"Reinitialised Phi-2 with temperature: {llm_temperature}", icon="❗"
            )

    _buttons = []

    # Friendly intro message, separate from the chat history
    with st.chat_message("ai", avatar="ollama_langchain_guide/src/phi.svg"):
        st.markdown(
            f"Hi! I'm Phi-2, your helpful LLM assistant. Ask me anything and I'll do my best to respond.\n\nWhy not try these questions to get started?"
        )
        _buttons.append(
            (
                st.button("Who was the first man on the Moon?"),
                "Who was the first man on the Moon?",
            )
        )
        _buttons.append(
            (
                st.button("Why is it called Edam Cheese?"),
                "Why is it called Edam Cheese?",
            )
        )
        _buttons.append(
            (
                st.button("How do you calculate digits of PI in Python?"),
                "How do you calculate digits of PI in Python?",
            )
        )

    # Display chat messages from history on app rerun
    for role, message in st.session_state.messages:
        # skip system prompt message
        if role == "system":
            continue
        # log all other messages with approriate avatars
        elif role == "human":
            avatar = "https://api.dicebear.com/7.x/thumbs/svg?seed=Kitty"
        else:
            avatar = "ollama_langchain_guide/src/phi.svg"

        with st.chat_message(role, avatar=avatar):
            st.markdown(message)

    current_chat_message = st.container()

    prompt = st.chat_input("What is up?", disabled=st.session_state.disabled)

    if prompt:
        chat(prompt)

    for button, value in _buttons:
        if button:
            chat(prompt=value)
