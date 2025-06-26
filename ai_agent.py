from dotenv import load_dotenv
load_dotenv()

import os
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)
    else:
        raise ValueError(f"Unsupported provider: {provider}")

    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    agent = create_react_agent(
        model=llm,
        tools=tools,
        
    )

    state = {
        "messages": [
            SystemMessage(content=system_prompt),
            HumanMessage(content=query)
        ]
    }
    response = agent.invoke(state)

    messages = response.get("messages", [])
    ai_messages = [msg.content for msg in messages if isinstance(msg, AIMessage)]

    return ai_messages[-1] if ai_messages else "No response received from agent."
