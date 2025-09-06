from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fetcher import fetch_cve
from analyzer import analyzer
from notifier import notifier_agent
#from fastapi.templating import Jinja2Templates


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

#templates = Jinja2Templates(directory="templates")

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
def view_analysis():
    try:
        results = analyzer()
        return {"message": "Analysis completed successfully!", "data": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/notify")
def notify_results():
    try:
        results=analyzer()
        msg=notifier_agent(results)
        return {"message": msg}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))