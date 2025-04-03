import requests
from dotenv import load_dotenv
import os
from fetcher import fetch_cve

load_dotenv()
api_key=os.getenv("OPENAIROUTER_key")
model=os.getenv("OPEN_MODEL")
res=fetch_cve()

def analyzer():
    url="https://openrouter.ai/api/v1/chat/completions"
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data={
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": f"Analyze the following vulnerabilities and provide a brief risk assessment for each {res['CVE_ID']} in {res}"
            }
        ],
    }
    response=requests.post(url, headers=headers, json=data)
    if response.status_code!=200:
        raise Exception(f"Failed to load page {response.status_code}")
    return response.json()