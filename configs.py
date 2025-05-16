import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "25230605"))
  API_HASH = os.environ.get("API_HASH", "b7d6c13e37d52cbbea25742f1c8b40cd")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "8173754492:AAEiZ2dv_tUtrEWwl9-wwWRsWV_eqkSRONU")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Mms_hub18_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "https://t.me/+K0ZqQxVEpCgyYWY1"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "bharatlinks.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "229853ecbbbbd01d73da405efce80c3acb8654ca")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "https://t.me/just_night13"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://facknet1999:GjMN6ZY5R3AbPx56@cluster0.6a3fnf0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](http://t.me/Mms_hub18_bot})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
