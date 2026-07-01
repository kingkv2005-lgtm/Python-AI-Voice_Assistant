# Python-AI-Chatbot

A voice-controlled Python assistant (Jarvis) that listens for spoken commands and responds using text-to-speech.

## Features

- Tells the current time
- Tells the current date
- Says its name when asked
- Searches Google for a spoken topic
- Searches YouTube for a spoken topic
- Exits when told to "exit"

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

## Usage

Once running, speak commands such as:
- "your name"
- "time" or "clock"
- "date" or "today"
- "search web"
- "search youtube"
- "exit"

## Requirements

- Python 3.x
- A working microphone
- Internet connection (uses Google Speech Recognition)
