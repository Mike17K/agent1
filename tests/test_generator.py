from core.generator import generate_with_context

if __name__ == "__main__":
    test_query = "What is the capital of France?"
    test_context = ["France is a country in Europe known for its history."]
    result = generate_with_context(test_query, test_context)
    print(result)