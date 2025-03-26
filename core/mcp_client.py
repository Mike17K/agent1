import requests

class MCPClient:
    def __init__(self, base_url="http://localhost:11434/api/generate", model="gemma3:4b"):
        self.base_url = base_url
        self.model = model

    def send_request(self, query: str, context: str):
        payload = {
            "model": self.model,
            "prompt": f"Query: {query}\nContext: {context}",
            "stream": False
        }
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(self.base_url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json().get("response", "No response from model")
        except requests.exceptions.RequestException as e:
            return f"Error: {e}"
