import requests
from PIL import Image
import os


def download_image(url: str, destination: str):

    with requests.get(
        url,
        stream=True,
        timeout=(3, 90),
    ) as response:

        response.raise_for_status()

        with open(destination, "wb") as f:

            for chunk in response.iter_content(chunk_size=65536):

                if chunk:
                    f.write(chunk)

    verify_image(destination)


def verify_image(path):

    try:

        with Image.open(path) as img:

            img.load()

    except OSError:

        os.remove(path)

        raise RuntimeError(
            "Downloaded image is corrupted."
        )