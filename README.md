# <img src="resources/ollama.png" style="height:32px;margin-bottom:-8px;"> + <img src="ollama_langchain_guide/src/phi.svg" style="height:32px;margin-bottom:-8px;"> ⇨ <img src="resources/langchain.png" style="height:32px;padding-right:20px;margin-bottom:-8px;"> Ollama LangChain Guide
 Develop LangChain using local LLMs with Ollama

* LLM costs getting you down?
* Want to develop offline?
* Don't want to share your personal data with LLM providers?
* Save costs, develop anywhere, and own all your data with Ollama and LangChain!

## Before you start

* This tutorial requires several terminals to be open and running proccesses at once i.e.: to run various Ollama servers.
* When you see the 🆕 emoji before a set of terminal commands, open a new terminal process.
* When you see the ♻️ emoji before a set of terminal commands, you can re-use the same terminal you used last time.

## Prerequisites

1. Download and install [Ollama](https://ollama.com/download) and start the server.

🆕
```sh
curl -fsSL https://ollama.com/install.sh | sh
ollama serve
```

2. Download and install [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer).

3. Fork this repository and setup the Poetry environment:

🆕
```sh
git clone https://github.com/Cutwell/ollama-langchain-guide.git
cd ollama-langchain-guide
poetry install
```

## Tutorial

1. Browse the [available Ollama models](https://ollama.com/library) and select a model.

* Think about your local computers available RAM and GPU memory when picking the model + quantisation level.
* We will be using the `phi-2` model from Microsoft ([Ollama](https://ollama.com/library/phi), [Hugging Face](https://huggingface.co/microsoft/phi-2)) as it is both small and fast.
* Read [this](https://www.promptingguide.ai/models/phi-2) summary for advice on prompting the `phi-2` model optimally.

♻️
```sh
ollama pull phi
```

2. Start the Ollama server.

* This server can be queried with LangChain, or you can interact with it in this terminal.

♻️
```sh
ollama run phi
```

3. Run the PyTest tests in `/ollama_langchain_guide/tests` to check everything is working correctly.

🆕
```sh
poetry run pytest -rP ollama_langchain_guide/tests
```

4. Get started building your own local LLM projects with the example StreamLit app in `/ollama_langchain_guide/src`.

♻️
```sh
poetry run streamlit run ollama_langchain_guide/src/app.py --server.port=8080
```

## Pros and Cons of Phi-2

|**Pros**|**Cons**|
|:---:|:---:|
|Natural language, human-like outputs.|Can distract itself, prone to creating logic puzzles based on user queries + tries to solve them itself.|
|Context window of 2048 tokens - can use chat history in answers.|Often ignores established facts in chat history - answers same question multiple ways in the same conversation.|
|Can output syntax-correct Python code.|Bad at generating code that achieves desired goal - e.g.: outputs a syntax-correct function to calculate Pi, but the outputs are garbage.|
|Very fast response time.||

## License
MIT
