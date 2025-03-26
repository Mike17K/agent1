from langchain_core.tools import Tool
from langchain_google_community import GoogleSearchAPIWrapper

search = GoogleSearchAPIWrapper()

webSearchTool = Tool(
    name="google_search",
    description="Search Google for recent results.",
    func=search.run,
)

def search_web(query):
    return webSearchTool.run(tool_input=query)