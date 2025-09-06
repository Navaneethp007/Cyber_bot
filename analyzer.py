import requests
from dotenv import load_dotenv
import os
from fetcher import fetch_cve
import json
import re

load_dotenv()
api_key=os.getenv("OPENAIROUTER_key") #currently expired
model=os.getenv("OPEN_MODEL")
res=fetch_cve()

def analyzer():
    url="https://openrouter.ai/api/v1/chat/completions"
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    str="\n".join([f"CVE ID: {item['id']}, Description: {item['description']}, Published Date: {item['published']} Last modified: {item['lastModified']}, Status:{item['status']}, Score:{item['score']}, Severity:{item['severity']}, References:{item['references']}" for item in res])
    data={
        "model": model,
        "temperature": 0.1,
        "messages": [
            {
                "role": "user",
                "content": f"Analyze the following vulnerability data: {str}. For each vulnerability, provide a brief risk assessment. Then, format the output as a nested JSON object where the top-level keys are risk categories (Critical, Moderate, Low) and under each category, map each CVE ID to its risk assessment and action to be taken."

            }
        ],
    }
    response=requests.post(url, headers=headers, json=data)
    if response.status_code!=200:
        raise Exception(f"Failed to load page {response.status_code}")
    raw_output = response.json()["choices"][0]["message"]["content"]
    cleaned_output = re.sub(r"```json\n|```", "", raw_output).strip() 

    try:
        return json.loads(cleaned_output) 
    except json.JSONDecodeError:
        raise Exception("Failed to parse LLM output as JSON")