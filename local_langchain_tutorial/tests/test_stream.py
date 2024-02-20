from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.llms import Ollama


def test_invoke():
    llm = Ollama(
        model="phi",
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    )
    print("User: The first man on the moon was ...")
    llm("The first man on the moon was ...")
