# A basic session manager for storing and retrieving context
session_context = {}

def get_context():
    return session_context.get("context", "")

def update_context(query: str, response: str):
    session_context["context"] = f"{session_context.get('context', '')}\nQuery: {query}\nResponse: {response}"