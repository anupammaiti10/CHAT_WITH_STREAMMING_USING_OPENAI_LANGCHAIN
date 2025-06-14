# CHAT_WITH_STREAMMING_USING_OPENAI_LANGCHAIN

A chat application demonstrating streaming responses using OpenAI and LangChain.

## Overview

This project leverages [LangChain](https://python.langchain.com/) and OpenAI’s language models to build an interactive chat application with real-time streaming of responses.

## Features

- **Streaming Responses:** Get real-time streaming outputs from OpenAI.
- **LangChain Integration:** Modular chaining of prompts, memory, and output.
- **Interactive App:** User-friendly interface for chatting with the LLM.

## LangChain Chaining

The chaining logic, implemented in the `chain.py` file (or update this to the correct filename), coordinates prompt templates, memory, and LLM calls. It enables flexible and extendable pipelines for processing chat messages.

**Key Points:**
- Prompts are structured for clarity and context retention.
- Memory modules store previous interactions for contextual continuity.
- Output is streamed for a responsive chat experience.

## App File

The main app logic resides in `app.py` (or update to the actual filename, e.g., `main.ipynb`). This file handles:
- User input and output display.
- Instantiation and management of the LangChain pipeline.
- Integration with the OpenAI API for generating responses.

## Getting Started

1. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your OpenAI API key:**
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

3. **Run the app:**
   ```bash
   python app.py
   # or for Jupyter Notebook
   jupyter notebook main.ipynb
   ```

## Folder Structure

```
.
├── app.py  # Main application file
├── chain.py               # LangChain logic (update filename as needed)
├requirements.txt
└── README.md
```

## License

MIT License.
