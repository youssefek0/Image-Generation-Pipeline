import base64
import os
import requests

from PIL import Image
from io import BytesIO

from config import (
    API_URL,
    API_KEY,
    DIMENSIONS,
    OUTPUT_FOLDER,
)


class ImageGenerator:

    def __init__(self):

        self.headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Accept": "application/json",
        }

    def generate(self, request):

        width, height = DIMENSIONS[request.aspect_ratio]

        payload = {
            "prompt": request.prompt,
            "negative_prompt": request.negative_prompt,
            "width": width,
            "height": height,
            "output_format": "png",
        }

        response = requests.post(
            API_URL,
            headers=self.headers,
            data=payload,
            timeout=(3, 90),
        )
        print(response.status_code)
        print(response.text)

        if response.status_code == 400:

            raise RuntimeError(
                "Prompt rejected by moderation."
            )

        if response.status_code == 403:

            raise RuntimeError(
                "Generation blocked."
            )

        response.raise_for_status()

        data = response.json()

        if "image" in data:

            self.save_base64(data["image"])

        elif "url" in data:

            from downloader import download_image

            download_image(
                data["url"],
                os.path.join(
                    OUTPUT_FOLDER,
                    "generated.png",
                ),
            )

        else:

            raise RuntimeError(
                "Unknown API response."
            )

    def save_base64(self, encoded):

        image = Image.open(
            BytesIO(base64.b64decode(encoded))
        )

        image.load()

        image.save(
            os.path.join(
                OUTPUT_FOLDER,
                "generated.png",
            )
        )