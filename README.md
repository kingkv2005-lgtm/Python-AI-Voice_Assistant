# Python AI Voice Assistant

## Overview

Python AI Voice Assistant is a desktop voice-controlled assistant developed using Python. It leverages speech recognition and text-to-speech technologies to execute voice commands such as telling the current time and date, searching Google and YouTube, and responding to basic conversational queries.

## Features

- Voice command recognition
- Text-to-speech responses
- Current time retrieval
- Current date retrieval
- Google search integration
- YouTube search integration
- Voice-triggered application exit

## Project Structure

```
Python-AI-Chatbot/
│
├── src/
│   ├── main.py       # Entry point, listens and responds to voice commands
│   └── utils.py       # Helper functions (speak, get_current_time, get_current_date, search_web, search_youtube)
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

1. Clone the repository
   ```
   git clone https://github.com/<your-username>/Python-AI-Chatbot.git
   cd Python-AI-Chatbot
   ```

2. Install dependencies
   ```
   pip install -r requirements.txt
   ```

   Note: `PyAudio` can be tricky to install on some systems.
   - Windows: `pip install pyaudio` usually works, or use `pipwin install pyaudio` if it fails.
   - macOS: `brew install portaudio` then `pip install pyaudio`
   - Linux: `sudo apt-get install python3-pyaudio` or `sudo apt-get install portaudio19-dev` then `pip install pyaudio`

3. Run the assistant
   ```
   python src/main.py
   ```

## Technologies Used

- Python
- SpeechRecognition
- pyttsx3
- PyAudio
- Webbrowser
- Datetime

## Usage

Once running, speak commands such as:
> What time is it?

> Tell me today's date

> Search Google for Python tutorials

> Search YouTube for machine learning

> Exit


## Requirements

- Python 3.10+
- Microphone
- Internet Connection
- Windows/macOS/Linux


## Future Improvements

- Natural Language Processing(NLP)
- Integration with Large Language Models (LLMs)
- Smart home device control
- Weather information
- Calendar integration
- Desktop application interface
