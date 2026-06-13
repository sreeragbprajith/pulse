import requests
from datetime import datetime
from pathlib import Path
import smtplib
import os
from email.message import EmailMessage


def get_weather():
    try:
        response = requests.get(
            "https://wttr.in/Thiruvananthapuram?format=3",
            timeout=10
        )
        return response.text
    except:
        return "Weather unavailable"


def get_quote():
    try:
        response = requests.get(
            "https://zenquotes.io/api/random",
            timeout=10
        )
        data = response.json()[0]
        return f"{data['q']} — {data['a']}"
    except:
        return "Keep learning and building."

def send_email(summary):

    email = os.environ["EMAIL_ADDRESS"]
    password = os.environ["EMAIL_PASSWORD"]

    msg = EmailMessage()

    msg["Subject"] = "Pulse Daily Summary"
    msg["From"] = email
    msg["To"] = email

    msg.set_content(summary)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email, password)
        smtp.send_message(msg)

    print("Email sent successfully!")


def save_summary():
    Path("summaries").mkdir(exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")

    summary = f"""
PULSE DAILY SUMMARY
===================

Date: {today}

WEATHER
--------
{get_weather()}

QUOTE OF THE DAY
----------------
{get_quote()}
"""

    filename = f"summaries/{today}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(summary)

    print("Summary saved:", filename)
    send_email(summary)

save_summary()
