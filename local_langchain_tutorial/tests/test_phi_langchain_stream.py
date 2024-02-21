from langchain_community.llms import Ollama


def test_phi_langchain_stream():
    llm = Ollama(
        model="phi",
    )

    print("The first man on the moon was ...")

    for tokens in llm.stream("The first man on the moon was ..."):
        print(tokens)
