from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "6435225"
# -------------------------------------------------------------
API_HASH = "4e984ea35f854762dcde906dce426c2d"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "7765142028:AAGPRPYB-KBw239ZOqx_U2fREn7ZPW0FYdc")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://sumiloo:<db_password>@react.fvqrg.mongodb.net/?retryWrites=true&w=majority&appName=react")
OWNER_ID = int(getenv("OWNER_ID", "1808943146"))
SUPPORT_GRP = "https://t.me/suMelody_vibes"
UPDATE_CHNL = "https://t.me/+VVeCnUdiTGg0MjZl"
OWNER_USERNAME = "@dear_sumi"
    
