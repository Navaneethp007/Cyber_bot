# from bs4 import BeautifulSoup
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
    params={"resultsPerPage": 50, 
            "pubStartDate": "2024-12-01T00:00:00.000",
            "pubEndDate": "2025-03-28T00:00:00.000"
            }
    response=requests.get(url, params=params)
    if response.status_code!=200:
        raise Exception(f"Failed to load page {response.status_code}")
    # return response.json()
    item=response.json().get("vulnerabilities", [])
    results=[]
    for i in item:
        cve_id=i.get("cve", {}).get("id", "N/A")
        description=i.get("cve", {}).get("descriptions", [])
        val=description[0].get("value", "N/A")
        status=i.get("cve", {}).get("vulnStatus", "N/A")
        pub_date=i.get("cve", {}).get("published", "N/A")
        last_mod=i.get("cve", {}).get("lastModified", "N/A")
        # score=[]
        # vendor=[]
        # if status=="Analyzed" or status=="Modified":
        #     metrics=i.get("metrics", {})
        #     cvss=metrics.get("cvssMetricV2", [])
        #     for s in cvss:
        #         score.append({
        #             "Impact score": s.get("impactScore", "N/A"),
        #             "Base severity": s.get("baseSeverity", "N/A"),
        #             "Exploitability score": s.get("exploitabilityScore", "N/A"),
        #             "CVSS Data": s.get("cvssData", {})
        #         })
        #     congigurations=i.get("configurations", {})
        #     nodes=congigurations.get("nodes", [])
        #     for node in nodes:
        #         for match in node.get("cpe_match", []):
        #             cpeuri=match.get("cpe23Uri", "N/A")
        #             parts=cpeuri.split(":")
        #             vendor.append({
        #                 "vendor": parts[3],
        #                 "product": parts[4],
        #                 "version": parts[5] if parts[5] else "N/A"
        #             })
        results.append({
            "CVE_ID": cve_id,
            "Published_Date": pub_date,
            "Last_Modified": last_mod,
            "Description": val,
            "Status": status,
            # "Vendor_products": vendor,
            # "Metrics": score
        })
    return results


                    

    
    