from decouple import config
from dotenv import load_dotenv

load_dotenv(override=True)

### Bot Settings
TELEGRAM_API_TOKEN = config("TELEGRAM_API_TOKEN", default="", cast=str)

### Default Thumbnail
DEFAULT_THUMBNAIL = (
    "https://i.pinimg.com/originals/2a/dc/b5/2adcb5b7d4783c60ae9e57b6b7458274.jpg"
)
