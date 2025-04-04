from fastapi import FastAPI, HTTPException
from fetcher import fetch_cve
from analyzer import analyzer


app = FastAPI(
    title="Cybersecurity Threat Intelligence Bot API",
    description="API service for scraping and delivering cybersecurity threat data.",
    version="0.1",
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Cybersecurity Threat Intelligence API Service!"}

@app.get("/fetch")
def fetch_results():
    try:
        results=fetch_cve()
        return {"message": "Fetched successfully!", "data": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/analyze")
def analyze_results():
    try:
        results=analyzer()
        return {"message": "Analysis completed successfully!", "data": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))