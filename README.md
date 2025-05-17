Speech Translator

This project is a speech-to-text translator built with Python. It allows you to speak into your microphone, converts the speech to text, translates it into your chosen language, and logs it into a CSV file.

Features:
- Converts spoken words into text using speech recognition.
- Translates the recognized text into a chosen language.
- Saves the original and translated text in a CSV file with a timestamp.

Technologies Used:
- Python
- speech_recognition
- googletrans
- pandas

How to Set Up and Run:

1. Make sure Python is installed on your system.
2. Install the required packages using pip:
   pip install speechrecognition googletrans pandas

3. Open your terminal or command prompt.
4. Run the script:
   python speechtotext_translator.py

5. Speak into your microphone when prompted.
6. The program will print your spoken text, translate it, and store it in a CSV log.

Folder Structure:
speech-translator/
├── README.md
├── speech_to_text.py
└── translation_log.csv

Sample Output:
You say: Hello, how are you?
Translation (Tamil): வணக்கம், நீங்கள் எப்படி இருக்கிறீர்கள்?

Notes:
- Works best on desktop with a microphone.
- Ideal to run in environments like VS Code or Anaconda.
- The CSV log helps keep a record of your translations.

Author:
[sepala varsha]
