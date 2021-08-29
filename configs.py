# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
𝐓𝐡𝐢𝐬 𝐢𝐬 𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭 𝐅𝐢𝐥𝐞𝐬 𝐒𝐭𝐨𝐫𝐞 𝐁𝐨𝐭!
𝐒𝐞𝐧𝐝 𝐦𝐞 𝐚𝐧𝐲 𝐟𝐢𝐥𝐞 𝐈 𝐰𝐢𝐥𝐥 𝐬𝐚𝐯𝐞 𝐢𝐭 𝐢𝐧 𝐦𝐲 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞. 𝐀𝐥𝐬𝐨 𝐰𝐨𝐫𝐤𝐬 𝐟𝐨𝐫 𝐜𝐡𝐚𝐧𝐧𝐞𝐥. 𝐀𝐝𝐝 𝐦𝐞 𝐭𝐨 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐚𝐬 𝐀𝐝𝐦𝐢𝐧 𝐰𝐢𝐭𝐡 𝐄𝐝𝐢𝐭 𝐏𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧, 𝐈 𝐰𝐢𝐥𝐥 𝐚𝐝𝐝 𝐒𝐚𝐯𝐞 𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐅𝐢𝐥𝐞 𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 & 𝐚𝐝𝐝 𝐒𝐡𝐚𝐫𝐚𝐛𝐥𝐞 𝐁𝐮𝐭𝐭𝐨𝐧 𝐋𝐢𝐧𝐤.

🤖 **𝐌𝐲 𝐍𝐚𝐦𝐞:** [𝐅𝐢𝐥𝐞 𝐒𝐭𝐨𝐫𝐞 𝐁𝐨𝐭](https://t.me/{BOT_USERNAME})

📝 **𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞:** [𝐏𝐲𝐭𝐡𝐨𝐧𝟑](https://www.python.org)

📚 **𝐋𝐢𝐛𝐫𝐚𝐫𝐲:** [𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦](https://docs.pyrogram.org)

📡 **𝐇𝐨𝐬𝐭𝐞𝐝 𝐨𝐧:** [𝐇𝐞𝐫𝐨𝐤𝐮](https://heroku.com)

🧑🏻‍💻 **𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫:** [@𝐏𝐫𝐞𝐝𝐚𝐭𝐨𝐫𝐇𝐚𝐜𝐤𝐞𝐫𝐳𝐙](https://t.me/PredatorHackerzZ) 

👥 **𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩:** [𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝 𝐒𝐮𝐩𝐩𝐨𝐫𝐭](https://t.me/TeleRoid14)

📢 **𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥:** [𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝 𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/TeleRoidGroup)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [@𝐏𝐫𝐞𝐝𝐚𝐭𝐨𝐫𝐇𝐚𝐜𝐤𝐞𝐫𝐳𝐙](https://t.me/PredatorHackerzZ) 

𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐢𝐬 𝐒𝐮𝐩𝐞𝐫 𝐍𝐨𝐨𝐛. 𝐉𝐮𝐬𝐭 𝐋𝐞𝐚𝐫𝐧𝐢𝐧𝐠 𝐟𝐫𝐨𝐦 𝐎𝐟𝐟𝐢𝐜𝐢𝐚𝐥 𝐃𝐨𝐜𝐬. 𝐀𝐧𝐝 𝐒𝐞𝐞𝐤𝐢𝐧𝐠 𝐇𝐞𝐥𝐩 𝐅𝐫𝐨𝐦 𝐏𝐫𝐨 𝐂𝐨𝐝𝐞𝐫𝐬\n**@TheTeleRoid**

𝐈𝐟 𝐘𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐃𝐨𝐧𝐚𝐭𝐞 𝐎𝐮𝐫 𝐇𝐚𝐫𝐝 𝐖𝐨𝐫𝐤. 𝐘𝐨𝐮 𝐂𝐚𝐧 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐓𝐡𝐞 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫. 

𝐀𝐥𝐬𝐨 𝐫𝐞𝐦𝐞𝐦𝐛𝐞𝐫 𝐭𝐡𝐚𝐭 𝐝𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐰𝐢𝐥𝐥 𝐃𝐞𝐥𝐞𝐭𝐞 𝐀𝐝𝐮𝐥𝐭 𝐂𝐨𝐧𝐭𝐞𝐧𝐭𝐬 𝐟𝐫𝐨𝐦 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞. 𝐒𝐨 𝐛𝐞𝐭𝐭𝐞𝐫 𝐝𝐨𝐧'𝐭 𝐒𝐭𝐨𝐫𝐞 𝐓𝐡𝐨𝐬𝐞 𝐊𝐢𝐧𝐝 𝐨𝐟 𝐓𝐡𝐢𝐧𝐠𝐬.

[𝐃𝐨𝐧𝐚𝐭𝐞 𝐍𝐨𝐰](https://www.paypal.me/AbhishekKumarIN47) (𝐏𝐚𝐲𝐏𝐚𝐥)
"""
	HOME_TEXT = """
𝐇𝐞𝐥𝐥𝐨, [{}](tg://user?id={})\n\n𝐓𝐡𝐢𝐬 𝐢𝐬 𝐚 𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭 **𝐅𝐢𝐥𝐞 𝐒𝐭𝐨𝐫𝐞 𝐁𝐨𝐭**.

𝐇𝐨𝐰 𝐓𝐨 𝐔𝐬𝐞 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭 & 𝐁𝐞𝐧𝐞𝐟𝐢𝐭𝐬??

📢 𝐒𝐞𝐧𝐝 𝐌𝐞 𝐀𝐧𝐲 𝐅𝐢𝐥𝐞 & 𝐈𝐭'𝐥𝐥 𝐁𝐞 𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐈𝐧𝐭𝐨 𝐌𝐲 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 & 𝐘𝐨𝐮 𝐆𝐞𝐭 𝐓𝐡𝐞 𝐅𝐢𝐥𝐞 𝐋𝐢𝐧𝐤.

⚠️ 𝐁𝐞𝐧𝐢𝐟𝐢𝐭: 𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐨𝐯𝐢𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥, 𝐓𝐡𝐞𝐧 𝐈𝐭𝐬 𝐔𝐬𝐞𝐟𝐮𝐥 𝐅𝐨𝐫 𝐘𝐨𝐮𝐫 𝐃𝐚𝐢𝐥𝐲 𝐔𝐬𝐚𝐠𝐞, 𝐘𝐨𝐮 𝐜𝐚𝐧 𝐒𝐞𝐧𝐝 𝐌𝐞 𝐘𝐨𝐮𝐫 𝐅𝐢𝐥𝐞 & 𝐈'𝐥𝐥 𝐒𝐞𝐧𝐝 𝐘𝐨𝐮 𝐓𝐡𝐞 𝐋𝐢𝐧𝐤 𝐎𝐟 𝐘𝐨𝐮𝐫 𝐅𝐢𝐥𝐞 𝐒𝐨 𝐘𝐨𝐮𝐫 𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐛𝐞𝐫𝐬 𝐂𝐚𝐧 𝐆𝐞𝐭 𝐓𝐡𝐞 𝐅𝐢𝐥𝐞 𝐅𝐫𝐨𝐦 𝐌𝐞 & 𝐘𝐨𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐖𝐢𝐥𝐥 𝐁𝐞 𝐒𝐚𝐟𝐞 𝐅𝐫𝐨𝐦 𝐂𝐎𝐏𝐘𝐑𝐈𝐆𝐇𝐓 𝐈𝐍𝐅𝐑𝐈𝐍𝐆𝐄𝐌𝐄𝐍𝐓 𝐈𝐬𝐬𝐮𝐞.

❌ 𝗣𝗢𝗥𝗡𝗢𝗚𝗥𝗔𝗣𝗛𝗜𝗖 𝗖𝗢𝗡𝗧𝗘𝗡𝗧𝗦 𝐀𝐫𝐞 𝐒𝐭𝐫𝐢𝐜𝐭𝐥𝐲 𝐏𝐫𝐨𝐡𝐢𝐛𝐢𝐭𝐞𝐝 & 𝐖𝐢𝐥𝐥 𝐆𝐞𝐭 𝐘𝐨𝐮 𝐁𝐚𝐧𝐧𝐞𝐝 𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭𝐥𝐲. 𝐈 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐀𝐥𝐬𝐨! 𝐂𝐡𝐞𝐜𝐤 **𝐀𝐛𝐨𝐮𝐭 𝐁𝐨𝐭** 𝐁𝐮𝐭𝐭𝐨𝐧.
"""
