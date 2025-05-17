#speech_to_text

import sys
import random
import speech_recognition as sr
from googletrans import Translator
import pandas as pd
import datetime

sys.stdout.reconfigure(encoding='utf-8')
listener = sr.Recognizer()
translator = Translator()
csv_file = "translation_log.csv"

def save_to_log(original, translated, lang_code):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    row = pd.DataFrame([{
        "Original Text": original,
        "Translated Text": translated,
        "Language": lang_code,
        "Timestamp": timestamp
    }])
    file_exists = pd.io.common.file_exists(csv_file)
    row.to_csv(csv_file, mode='a', header=not file_exists, index=False)

def ask_language():
    lang = input(" Pick a language to translate to (e.g., hi for Hindi, ta for Tamil): ").strip()
    return lang if lang else 'en'

def translate_from_speech():
    lang_code = ask_language()
    with sr.Microphone() as mic:
        print("\n Listening... speak now!")
        listener.adjust_for_ambient_noise(mic)
        try:
            audio = listener.listen(mic)
            user_input = listener.recognize_google(audio)
            print(f" You said: \"{user_input}\"")

            translated = translator.translate(user_input, dest=lang_code)
            print(f" In '{lang_code}', that's: \"{translated.text}\"")

            save_to_log(user_input, translated.text, lang_code)
            print(" Translation saved to your log.")

        except sr.UnknownValueError:
            print(" Hmm, couldn’t understand. Wanna try again?")
        except sr.RequestError as err:
            print(f" Service error: {err}")

def run_translator():
    print(" Hey! Ready to speak and translate?")
    while True:
        translate_from_speech()
        again = input("\nWanna try another one? (y/n): ").strip().lower()
        if again not in ['y', 'yes']:
            print(" All done. Take care!")
            break

if __name__ == "__main__":
    run_translator()
