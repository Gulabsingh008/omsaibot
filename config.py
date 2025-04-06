import datetime
from os import environ 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

class Config:
    API_ID = environ.get("API_ID", "")
    API_HASH = environ.get("API_HASH", "")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "Auto_Forward") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://bikash:bikash@bikash.3jkvhp7.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7170452349').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "-1002657472890") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")
    PORT = environ.get('PORT', '8080')
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
