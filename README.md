# Image Generation Pipeline

## Overview

This project implements a production-style **text-to-image generation pipeline** in Python. It accepts a natural language prompt, sends it to an image generation API, processes the response, verifies the integrity of the generated image, and saves it locally.

The primary goal of this project is to demonstrate robust API integration rather than image generation itself. It focuses on software engineering practices such as resilient networking, error handling, binary data processing, and clean project architecture.

---

## Features

* Text-to-image generation using a real image generation API
* Support for user prompts
* Optional negative prompts
* Aspect ratio selection (1:1, 16:9, 9:16)
* Mapping of aspect ratios to API-supported image dimensions
* Connection and read timeouts
* Retry logic with exponential backoff
* Graceful handling of API errors and moderation responses
* Streaming image downloads to avoid loading large files into memory
* Image integrity verification using Pillow
* Local image storage

---

## Project Structure

```text
image_generation_pipeline/
│
├── app.py                 # Entry point
├── config.py              # Configuration and environment variables
├── image_client.py        # API communication
├── downloader.py          # Image download and verification
├── models.py              # Data models
├── utils.py               # Retry and helper utilities
├── outputs/               # Generated images
├── requirements.txt
├── .env
└── .gitignore
```

---

## Technologies Used

* Python 3
* Requests
* Pillow
* python-dotenv
* Tenacity

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd image_generation_pipeline
```

Create and activate a virtual environment.

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root.

Example:

```text
API_KEY=your_api_key_here
```

Replace the placeholder with your image generation API key.

---

## Running the Project

Run the application:

```bash
python app.py
```

You will be prompted to enter:

* Image prompt
* Negative prompt (optional)
* Aspect ratio

The generated image will be verified and saved inside the `outputs` directory.

---

## Error Handling

The application is designed to handle common production scenarios, including:

* Invalid API responses
* Network connection failures
* Request timeouts
* Rate limiting
* Service unavailability
* Prompt moderation failures
* Corrupted or incomplete image downloads

---

## Image Verification

Every generated image is validated before being accepted.

The verification process:

1. Saves the image locally.
2. Opens the image using Pillow.
3. Forces a complete pixel decode.
4. Detects truncated or corrupted files.
5. Rejects invalid images instead of silently saving them.

---

## Learning Objectives

This project demonstrates:

* REST API integration
* HTTP request handling
* Timeout management
* Retry strategies
* Streaming binary downloads
* File integrity verification
* Environment variable management
* Clean Python project organization

---

## Future Improvements

* Support multiple image generation providers
* Batch image generation
* Graphical user interface
* Command-line arguments
* Structured logging
* Unit and integration tests
* Docker support
* Asynchronous request handling

---

## License

This project is intended for educational and portfolio purposes.
