from langchain_community.llms import Ollama


def test_invoke():
    llm = Ollama(model="phi")
    response = llm("The first man on the moon was ...")
    print(f"User: The first man on the moon was ...\n{response}")
