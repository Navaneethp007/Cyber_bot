import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
import requests

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "nvps742@gmail.com"
SENDER_PASSWORD = os.getenv("APP_PASSWORD")
RECIPIENTS = ["psprapha@gmail.com"]
api_key = os.getenv("OPENAIROUTER_key")
model = os.getenv("OPEN_MODEL")

def send_notification(subject, body):
    llm_url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    raw_data = f"Subject: {subject}\nBody: {body}"
    data = {
        "model": model,
        "temperature": 0.3, 
        "messages": [
            {
                "role": "user",
                "content": (
                    f"Generate a concise email subject and body for a critical CVE alert based on this data: {raw_data}. "
                    f"Return exactly this format: 'Subject: Critical CVE Alert: CVE ID - <brief risk>'\n'Body: <3-sentence summary including CVE ID, risk, and action>'"
                )
            }
        ],
    }
    response = requests.post(llm_url, headers=headers, json=data)
    if response.status_code != 200:
        raise Exception(f"LLM failed: {response.status_code}")

    llm_output = response.json()["choices"][0]["message"]["content"].strip()
    sub, bod = llm_output.split("\nBody: ", 1)
    sub = sub.replace("Subject: ", "")
    msg = MIMEText(bod)
    msg["Subject"] = sub
    msg["From"] = SENDER_EMAIL
    msg["To"] = ", ".join(RECIPIENTS)
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        return f"Failed to send notification: {e}"

def notifier_agent(analyzed_data):
    critical_cves = analyzed_data.get("Critical", {})
    for cve_id, det in critical_cves.items():
        subject = f"Critical CVE Alert: {cve_id}"
        body = f"CVE: {cve_id}\nRisk Assessment: {det['Risk Assessment']}\nAction: {det['Action']}"
        send_notification(subject, body)
    return "Notification sent successfully!"

