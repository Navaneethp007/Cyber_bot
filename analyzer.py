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
    str="\n".join([f"CVE ID: {item['CVE_ID']}, Description: {item['Description']}, Published Date: {item['Published_Date']} Last modified: {item['Last_Modified']}, Status:{item['Status']}" for item in res])
    data={
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": f"Analyze the following vulnerabilities with their details and provide a brief risk assessment for each item in {str}"
            }
        ],
    }
    response=requests.post(url, headers=headers, json=data)
    if response.status_code!=200:
        raise Exception(f"Failed to load page {response.status_code}")
    return response.json()["choices"][0]["message"]["content"]