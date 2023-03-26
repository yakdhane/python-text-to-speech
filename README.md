Sure, here is the README.md file:

# Python Text-to-Speech Application

[![Python Version](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/release/python-390/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/username/repo/blob/master/LICENSE)

This is a Python application that converts text to speech using open-source AI models. The application uses the gTTS library to generate an audio file from the given text and then converts the audio file to a numpy array using the pydub library.

## Installation

To install the dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To use the application, run the `app.py` file and enter the text you want to convert to speech when prompted.

```bash
python app.py
```

## Docker

To run the application using Docker, first build the Docker image using the following command:

```bash
docker build -t text-to-speech .
```

Then, run the Docker container using the following command:

```bash
docker run -p 5000:5000 text-to-speech
```

## Files

- `app.py`: The main Python file that contains the code for the text-to-speech application.
- `requirements.txt`: The file that contains the Python dependencies required to run the application.
- `Dockerfile`: The file that contains the instructions to build a Docker image of the application.