# https://t.me/ultroid_official

import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

# Load .env file
load_dotenv(".env")

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
 
BAN = int(os.environ.get("BAN", "0")) #Owner user id - dont chnge 
OWNER = os.environ.get("OWNER", "Ownerrrrrrrrrrrrrrrrrr") #Owner username
OWNER_ID = int(os.environ.get("OWNER_ID", "6147843565")) #Owner user id
OWNER_USERNAME = os.environ.get('OWNER_USERNAME', 'Admin')
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "x") # WITHOUR @
CHANNEL = os.environ.get("CHANNEL", "x") # WITHOUR @

#auto delete
DELETE_AFTER = int(os.environ.get("DELETE_AFTER", 1200)) #seconds
NOTIFICATION_TIME = int(os.environ.get('NOTIFICATION_TIME', 60)) #seconds
AUTO_DELETE = os.environ.get("AUTO_DELETE", True) #ON/OFF
GET_AGAIN = os.environ.get("GET_AGAIN", False) #ON/OFF
DELETE_INFORM = os.environ.get("INFORM" , None)
NOTIFICATION = os.environ.get("NOTIFICATION" ,"⚠️File will delete after 30sec.")
GET_INFORM = os.environ.get("GET_INFORM" ,"File was deleted after {DELETE_AFTER} seconds. Use the button below to GET FILE AGAIN.")

#Premium varibles
PAYMENT_QR = os.getenv('PAYMENT_QR', 'https://ibb.co/rb6vnwZ')
PAYMENT_TEXT = os.getenv('PAYMENT_TEXT', '<b>- ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs - \n\n'
                                      '- 20ʀs - 1 ᴡᴇᴇᴋ\n- 50ʀs - 1 ᴍᴏɴᴛʜ\n'
                                      '- 100ʀs - 3 ᴍᴏɴᴛʜs\n- 300ʀs - 6 ᴍᴏɴᴛʜs\n\n'
                                      '🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs 🎁\n\n'
                                      '○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋ\n'
                                      '○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs\n○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ\n'
                                      '✨ ᴜᴘɪ ɪᴅ - <code>dm : @_____ for upi</code>\n\n'
                                      'ᴄʟɪᴄᴋ ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ /myplan\n\n'
                                      '💢 ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ\n\n'
                                      '‼️ ᴀғᴛᴇʀ sᴇɴᴅɪɴɢ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴜs sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ</b>')


DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "")

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002427274779")) #database save channel id 
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "0"))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "0"))

#Shortner (token system) db_channel
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "offerlinks.in") 
SHORTLINK_API = os.environ.get("SHORTLINK_API", "2b491547a49b1d8274e9a619c8258029ef2b8bd0")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "None")
TUT_VID = os.environ.get("TUT_VID", "https://t.me")

# ignore this one
SECONDS = int(os.getenv("SECONDS", "200")) # auto delete in seconds

PORT = os.environ.get("PORT", "8083")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")

try:
    ADMINS=[6147843565]
    for x in (os.environ.get("ADMINS", "6147843565").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")


FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "Caption") # remove None and fo this ->: "here come your txt" also with this " " 

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "True") == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot !"

ADMINS.append(OWNER_ID)
ADMINS.append(6147843565)

LOG_FILE_NAME = "uxblogs.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# https://t.me/ultroid_official
