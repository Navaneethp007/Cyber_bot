import requests
from dotenv import load_dotenv
import os
from fetcher import fetch_cve
import json

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
                "content": f"Analyze the following vulnerability data: {str}. For each vulnerability, provide a brief risk assessment. Then, format the output as a nested JSON object where the top-level keys are risk categories (Critical, Moderate, Low) and under each category, map each CVE ID to its risk assessment."

            }
        ],
    }
    response=requests.post(url, headers=headers, json=data)
    if response.status_code!=200:
        raise Exception(f"Failed to load page {response.status_code}")
    return response.json()["choices"][0]["message"]["content"]