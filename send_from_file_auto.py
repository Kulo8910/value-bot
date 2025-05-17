
import time
import telegram
from datetime import datetime

TOKEN = "7543856031:AAHD7fmHEa-2AycFmidDxZkg8ZxDbxKR86I"
CHAT_ID = 5686594211  # ← Sau khi chạy get_chat_id.py, thay bằng số Chat ID thật (không có dấu ngoặc kép)
FILE_PATH = "value_bet.txt"
CHECK_INTERVAL = 300  # 5 phút

sent_lines = set()

def extract_value_percent(line):
    try:
        percent_str = line.strip().split("|")[-1].replace("%", "").strip()
        return float(percent_str)
    except:
        return 0.0

def read_and_filter_lines():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()
        return [line.strip() for line in lines if extract_value_percent(line) > 10]
    except FileNotFoundError:
        print(f"[{datetime.now()}] ❌ File not found: {FILE_PATH}")
        return []

def send_new_bets(bot, lines):
    for line in lines:
        if line not in sent_lines:
            try:
                bot.send_message(chat_id=CHAT_ID, text=line)
                print(f"[{datetime.now()}] ✅ Sent: {line}")
                sent_lines.add(line)
            except Exception as e:
                print(f"[{datetime.now()}] ❌ Error sending message: {e}")

if __name__ == "__main__":
    print(f"[{datetime.now()}] 🚀 Auto bot started. Checking every {CHECK_INTERVAL} seconds.")
    bot = telegram.Bot(token=TOKEN)
    while True:
        lines_to_send = read_and_filter_lines()
        send_new_bets(bot, lines_to_send)
        time.sleep(CHECK_INTERVAL)
