import requests
from datetime import datetime
from pathlib import Path

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

def save_summary():
    Path("summaries").mkdir(exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")

    summary = f"""
PULSE DAILY SUMMARY
===================

Date: {today}

Quote of the Day
----------------
{get_quote()}
"""

    filename = f"summaries/{today}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(summary)

    print("Summary saved:", filename)

save_summary()