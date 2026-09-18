from datetime import datetime

from langchain_core.tools import tool
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper


@tool
def save_to_txt(data: str, filename: str = "research_output.txt") -> str:
    """Save research data to a text file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = (
        f"--- Research Output ---\n"
        f"Timestamp: {timestamp}\n\n"
        f"{data}\n\n"
    )

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"


@tool
def search_web(query: str) -> str:
    """Search the web for information."""
    search = DuckDuckGoSearchRun()
    return search.run(query)


api_wrapper = WikipediaAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=100,
)

wiki_tool = WikipediaQueryRun(
    api_wrapper=api_wrapper
)

save_tool = save_to_txt
search_tool = search_web