import os

from config import OUTPUT_FOLDER
from image_client import ImageGenerator
from models import ImageRequest


def main():

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    prompt = input("Prompt: ")

    negative = input(
        "Negative prompt (optional): "
    )

    aspect = input(
        "Aspect (1:1 / 16:9 / 9:16): "
    )

    request = ImageRequest(
        prompt=prompt,
        negative_prompt=negative,
        aspect_ratio=aspect,
    )

    generator = ImageGenerator()

    try:

        generator.generate(request)

        print("Image saved successfully.")

    except Exception as e:

        print(e)


if __name__ == "__main__":
    main()
