# EmotionDetection

This is a Python Flask web application that uses IBM Watson NLP's Emotion Detection service to analyze emotions from a given text input. 
It detects emotions like **anger**, **disgust**, **fear**, **joy**, and **sadness**, and returns the emotion scores along with a **dominant emotion**.

---

## Features

- Emotion analysis using IBM Watson NLP API
- Flask web server endpoint `/emotionDetector`
- Error handling for blank or malformed input
- Unit tests for validation
- Pylint-compliant (score: 10/10)

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/EmotionDetection.git
cd EmotionDetection/final_project
```

### 2. Install the Dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the server
```bash
python3 server.py
```

### Running the tests
```bash
python3 test_emotion_detection.py
```

### License
This project is for educational purposes only and not intended for production use.