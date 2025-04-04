# from bs4 import BeautifulSoup
import requests

def fetch_cve():
    url="https://services.nvd.nist.gov/rest/json/cves/2.0"
    params={"resultsPerPage": 50, 
            "pubStartDate": "2024-12-01T00:00:00.000",
            "pubEndDate": "2025-03-28T00:00:00.000"
            }
    reresponse=requests.get(url, params=params)
    if reresponse.status_code!=200:
        raise Exception(f"Failed to load page {reresponse.status_code}")
    
    item=reresponse.json().get("vulnerabilities", [])
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
    # return results


