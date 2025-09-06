from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fetcher import fetch_cve
from analyzer import analyzer
from notifier import notifier_agent
from vector import store_in_vector_db, query_vector_db
# from fastapi.templating import Jinja2Templates
import requests
import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
model = os.getenv("OPEN_MODEL")
api_key = os.getenv("OPENAIROUTER_key")  

res = analyzer()
collection = store_in_vector_db(res)

app = FastAPI(
    title="Cybersecurity Threat Intelligence Bot API",
    description="API service for scraping and delivering cybersecurity threat data.",
    version="0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    query: str

# templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Cybersecurity Threat Intelligence API Service!"}

@app.get("/fetch")
def fetch_results():
    try:
        results = fetch_cve()
        return {"message": "Fetched successfully!", "data": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/analysis")
def analysis():
    try:
        results = analyzer()
        return {"message": "Analysis completed successfully!", "data": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/notify")
def notify():
    try:
        results = analyzer()
        msg = notifier_agent(results)
        return {"message": msg}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat")
def chat(request: ChatRequest):
    try:
        query = request.query
        results = query_vector_db(collection, query)
        
        if not api_key:
            return {"error": "OpenRouter API key not available"}
            
        llm_url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}", 
            "Content-Type": "application/json"
        }
        data = {
            "model": model,
            "temperature": 0.3,
            "messages": [
                {
                    "role": "user",
                    "content": (
                        f"User query: {query}\n"
                        f"Relevant CVE analysis data from ChromaDB: {results}\n"
                        "Provide a concise response to the user's query based on this data."
                    )
                }
            ],
        }
        
        response = requests.post(llm_url, headers=headers, json=data)
        if response.status_code != 200:
            return {"error": f"LLM failed: {response.status_code} - {response.text}"}
        
        llm_output = response.json()["choices"][0]["message"]["content"].strip()
        return {"response": llm_output}
        
    except Exception as e:
        return {"error": f"Chat failed: {str(e)}"}