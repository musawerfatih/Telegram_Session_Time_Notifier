import time
import requests
from datetime import datetime, timedelta
import pytz

# 🔹 Telegram Bot Credentials
# TELEGRAM_TOKEN = "jdflkjsdlkfj"
# CHAT_ID = "00000"

# 🔹 Define Trading Session Timings (Pakistan Time - UTC+5)
LONDON_OPEN = "13:00"  # 1:00 PM PKT
NEW_YORK_OPEN = "17:00"  # 5:00 PM PKT

# 🔹 Function to Send Telegram Alerts
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=payload)

# 🔹 Function to Check Time and Send Alerts
def check_trading_sessions():
    pakistan_tz = pytz.timezone("Asia/Karachi")
    now = datetime.now(pakistan_tz).strftime("%H:%M")
    
    if now == LONDON_OPEN:
        send_telegram_message("🚀 London Session has started! Time to scalp!")
    elif now == (datetime.strptime(LONDON_OPEN, "%H:%M") - timedelta(minutes=10)).strftime("%H:%M"):
        send_telegram_message("⏳ 10 minutes left for London Open! Get ready!")
    
    if now == NEW_YORK_OPEN:
        send_telegram_message("🔥 New York Session has started! Time to scalp!")
    elif now == (datetime.strptime(NEW_YORK_OPEN, "%H:%M") - timedelta(minutes=10)).strftime("%H:%M"):
        send_telegram_message("⏳ 10 minutes left for New York Open! Get ready!")

# 🔹 Send Confirmation Message When Bot Starts
send_telegram_message("✅ Trading Alert Bot is now running and checking for trading sessions!")

# 🔹 Run the Alert Bot Continuously
while True:
    check_trading_sessions()
    time.sleep(60)  # Check every minute















"""
You can directly send message to your bot from the browser using below link
https://api.telegram.org/botyour_telegram_bot_token/sendMessage?chat_id=your_chat_id_here&text=Test
https://api.telegram.org/bot7657132098:AAFm36C0LwIlEpzq5Gg_ayzem1_96EbooJM/sendMessage?chat_id=7425571871&text=Test
"""