# LangGraph AI Agent

An AI chatbot API built with FastAPI leveraging LangGraph, LangChain, and multiple LLM providers (Groq, OpenAI). It supports dynamic model selection and integrates a search tool (Tavily) to enhance responses.

---

## Features

- Supports multiple LLM providers: Groq and OpenAI.
- Dynamic model selection via API request.
- Integrated search tool (Tavily) to provide up-to-date information.
- Friendly and customizable system prompt.
- Built with FastAPI for quick, async API serving.
- Easy-to-use Swagger UI for interactive API testing.

---

## Tech Stack

- Python 3.9+
- [FastAPI](https://fastapi.tiangolo.com/) - Web framework
- [LangChain](https://python.langchain.com/) - LLM orchestration
- [LangGraph](https://github.com/langgraph/langgraph) - Agent orchestration
- [Groq](https://groq.com/) - LLM provider
- [OpenAI](https://openai.com/) - LLM provider
- [Tavily Search](https://tavily.com/) - Search tool integration
- [Uvicorn](https://www.uvicorn.org/) - ASGI server

---

## Setup

1. Clone the repository

```bash
git clone https://github.com/yourusername/langgraph-ai-agent.git
cd langgraph-ai-agent
