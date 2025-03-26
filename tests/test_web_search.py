from dotenv import load_dotenv 
load_dotenv()

from core.web_search import search_web

if __name__ == "__main__":
    print(search_web("What are the latest updates in AI?"))