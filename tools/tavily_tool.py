from tavily import TavilyClient
import os
from dotenv import load_dotenv


load_dotenv()
client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY"),
)
def tavily_search(query: str):
    """
    Search for a query using Tavily API.

    Args:
        query (str): The search query.
    """
    response = client.search(query, max_results=5)
    results = []

    for i, resi in enumerate(response['results']):
        title = resi.get('title', 'No title')
        url = resi.get('url', 'No URL')
        snippet = resi.get("content", '').strip()

        if len(snippet) > 300:
            snippet = snippet[:300] + "..."

        results.append(f"{i + 1}.\t{title}\n\tURL: {url}\n\tSnippet: {snippet}\n")
    return "\n\n".join(results)

