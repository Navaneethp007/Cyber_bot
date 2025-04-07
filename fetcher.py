
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("OPENAIROUTER_key")
model=os.getenv("OPEN_MODEL")

def fetch_cve():
    url="https://services.nvd.nist.gov/rest/json/cves/2.0"
    params={"resultsPerPage": 20, 
            "pubStartDate": "2024-12-01T00:00:00.000",
            "pubEndDate": "2025-03-28T00:00:00.000"
            }
    response=requests.get(url, params=params)
    if response.status_code!=200:
        raise Exception(f"Failed to load page {response.status_code}")
    # llm_url="https://openrouter.ai/api/v1/chat/completions"
    # headers={
    #     "Authorization": f"Bearer {api_key}",
    #     "Content-Type": "application/json"
    # }
    # data={
    #     "model": model,
    #     "messages": [
    #         {
    #             "role": "user",
    #             "content": f"Parse this raw NVD JSON into a clean JSON list with CVE_ID, Description, Status, Published Date, Last Modified Date and CVSS_Score. Make sure to parse it in descending order of published date. {response.json()}"
    #         }
    #     ],
    # }
    # llm_response=requests.post(llm_url, headers=headers, json=data)
    # if llm_response.status_code!=200:
    #     raise Exception(f"Failed to load page {llm_response.status_code}")
    # data=llm_response.json()["choices"][0]["message"]["content"]
    # i=data.find("[")
    # j=data.rfind("]")
    # return data[i:j+1]
    
    item=response.json().get("vulnerabilities", [])
    results=[]
    for i in item:
        cve_id=i.get("cve", {}).get("id", "N/A")
        description=i.get("cve", {}).get("descriptions", [])
        val=description[0].get("value", "N/A")
        status=i.get("cve", {}).get("vulnStatus", "N/A")
        pub_date=i.get("cve", {}).get("published", "N/A")
        last_mod=i.get("cve", {}).get("lastModified", "N/A")
        results.append({
            "CVE_ID": cve_id,
            "Description": val,
            "Published_Date": pub_date,
            "Last_Modified": last_mod,
            "Status": status
        })
    
    return results



