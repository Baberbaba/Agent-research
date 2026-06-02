from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from tools import search_tool, wiki_tool, save_tool
import os

load_dotenv()

# LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

# Tools
tools = [search_tool, wiki_tool, save_tool]

# Create agent (this handles tool execution automatically)
agent = create_agent(
    model=llm,
    tools=tools
)

# Query
query = "When and how did World War 1 start?"

# Run agent
response = agent.invoke({
    "messages": [("user", query)]
})

# Final answer
print(response["messages"][-1].content)