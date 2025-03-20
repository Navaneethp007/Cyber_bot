from fastapi import FastAPI, HTTPException
from scraper import scrape_data

app = FastAPI(
    title="Cybersecurity Threat Intelligence Bot API",
    description="API service for scraping and delivering cybersecurity threat data.",
    version="0.1",
)

@app.post("/")
def read_root():
    return {"message": "Welcome to the Cybersecurity Threat Intelligence API Service!"}

@app.get("/scrape")
def scrape():
    try:
        scrape_results=scrape_data()
        return {"message": "Scraping completed successfully!", "data": scrape_results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))