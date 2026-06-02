from langchain_core.tools import tool
from duckduckgo_search import DDGS

@tool
def search_tool(query: str) -> str:
    """Search the web"""
    return str(DDGS().text(query, max_results=3))


@tool
def wiki_tool(query: str) -> str:
    """Safe Wikipedia-style answer using DuckDuckGo fallback"""
    try:
        results = DDGS().text(f"{query} wikipedia", max_results=3)
        return str(results)
    except Exception as e:
        return f"Search failed: {str(e)}"


@tool
def save_tool(content: str) -> str:
    """Save output"""
    with open("research_output.txt", "a", encoding="utf-8") as f:
        f.write(content + "\n\n")
    return "Saved successfully"