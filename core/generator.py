# from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# model_name = "facebook/bart-large"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# def generate_with_context(query: str, retrieved_data: list):
#     context = " ".join(retrieved_data)
#     input_text = f"Query: {query}\nContext: {context}"
#     inputs = tokenizer.encode(input_text, return_tensors="pt", truncation=True)
#     outputs = model.generate(inputs, max_length=200)
#     return tokenizer.decode(outputs[0], skip_special_tokens=True)

from core.mcp_client import MCPClient

client = MCPClient()

def generate_with_context(query: str, retrieved_data: list):
    context = " ".join(retrieved_data)
    return client.send_request(query, context)