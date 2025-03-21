from bs4 import BeautifulSoup
import requests

# def scrape_data():
#     URL = "https://www.cvedetails.com/vulnerability-list.php"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
#         "Accept-Encoding": "gzip, deflate",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#         "Accept-Language": "en-US,en;q=0.5",
#         "Referer": "https://www.cvedetails.com/vulnerability-list.php",
#     }
#     response=requests.get(URL, headers=headers)
#     if response.status_code!=200:
#         raise Exception(f"Failed to load page {response.status_code} ")
#     soup=BeautifulSoup(response.text, 'html.parser')
#     vul=[]
#     tab_rows=soup.select("table#vulnslisttable tr")[1:]
#     for row in tab_rows:
#        columns=row.find_all('td')
#        if len(columns)>1:
#            vul.append({
#                "CVE_ID": columns[0].text.strip(),
#                "Description": columns[1].text.strip(),
#                "Severity": columns[2].text.strip(),
#            })
#     return vul

def fetch_cve():
    url="https://services.nvd.nist.gov/rest/json/cves/2.0"
    params={"resultsPerPage": 10, 
            "pubStartDate": "2025-01-01T00:00:00.000",
            "pubEndDate": "2025-02-28T00:00:00.000"
            }
    response=requests.get(url, params=params)
    if response.status_code!=200:
        raise Exception(f"Failed to load page {response.status_code}")
    # return response.json()
    item=response.json()
    
    