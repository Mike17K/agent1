from dotenv import load_dotenv 
load_dotenv()

from fastapi import FastAPI
from app.api import router

app = FastAPI()

# Include API endpoints
app.include_router(router)

@app.get("/")
def welcome():
    return {"message": "Welcome to the AI Agent using MCP principles!"}
