from dataclasses import dataclass


@dataclass
class ImageRequest:
    prompt: str
    aspect_ratio: str = "1:1"
    negative_prompt: str = ""