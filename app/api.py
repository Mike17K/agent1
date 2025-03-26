from pydantic import BaseModel
from fastapi import APIRouter
from core.web_search import search_web
from core.retriever import retrieve_with_context
from core.generator import generate_with_context
from core.session_manager import update_context, get_context

router = APIRouter()

@router.get("/search/")
def web_search(query: str):
    return search_web(query)

class QueryRequest(BaseModel):
    query: str

@router.post("/generate/")
def generate(request: QueryRequest):
    query = request.query
    context = get_context()
    retrieved_data = retrieve_with_context(query, context)
    response = generate_with_context(query, retrieved_data)
    update_context(query, response)
    return {"response": response}