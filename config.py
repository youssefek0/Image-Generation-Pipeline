import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HF_API_KEY")

API_URL = "https://router.huggingface.co/fal-ai/fal-ai/flux/schnell"
OUTPUT_FOLDER = "outputs"

DIMENSIONS = {
    "1:1": (1024, 1024),
    "16:9": (1344, 768),
    "9:16": (768, 1344)
}

CONNECT_TIMEOUT = 3
READ_TIMEOUT = 90