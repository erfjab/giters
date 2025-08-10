from decouple import config
from dotenv import load_dotenv

load_dotenv(override=True)

### Bot Settings
TELEGRAM_API_TOKEN = config("TELEGRAM_API_TOKEN", default="", cast=str)
