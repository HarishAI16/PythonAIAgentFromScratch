from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

llm = ChatOpenAI(
    model="gpt-5.6-luna",
    reasoning_effort="none"
)

tools = [search_tool, wiki_tool, save_tool]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
    You are a research assistant that helps generate research papers.

    Answer the user's query using the available tools when necessary.
    Provide a clear and useful research response.
    """
)

query = input("What can I help you research? ")

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": query
            }
        ]
    }
)

print("\n--- Research Result ---")
print(result["messages"][-1].content)