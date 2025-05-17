
import telegram

TOKEN = "7543856031:AAHD7fmHEa-2AycFmidDxZkg8ZxDbxKR86I"
bot = telegram.Bot(token=TOKEN)

updates = bot.get_updates()
for u in updates:
    print("Chat ID:", u.message.chat.id)
