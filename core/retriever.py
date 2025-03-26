from .web_search import webSearchTool

def retrieve_with_context(query: str, context: str) -> list[str]:
    # Combine query and context
    full_query = f"{query} {context}"
    # Use the Google Search tool
    return [webSearchTool.run(tool_input=full_query)]