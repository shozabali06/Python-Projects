import speech_recognition as sr
import requests
import pygame
import os
import webbrowser
import pyttsx3
from music_library import play_music
from gtts import gTTS
from news import play_news
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')
def get_news():
    url = (f'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={api_key}')
    response = requests.get(url)
    data = response.json()
    
    titles_and_descriptions = []
    for article in data['articles']:
        title = article.get('title')
        description = article.get('description')
        titles_and_descriptions.append({'title': title, 'description': description})
    
    return titles_and_descriptions

def speak_text(text, filename):
    tts = gTTS(text=text, lang='en')
    if os.path.exists(filename):
        os.remove(filename)
    tts.save(filename)

def play(file):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    # Wait for the music to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.stop()
    pygame.mixer.quit()


def play_news():
    if __name__ == "__main__":
        news = get_news()
        for i, article in enumerate(news):
            title = article.get('title')
            description = article.get('description')
            text = f"Title: {title}\nDescription: {description}"
            
            filename = "temp.mp3"
            speak_text(text, filename)
            play(filename)
            
            # Remove the mp3 file after playing to clean up
            if os.path.exists(filename):
                os.remove(filename)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open_social_media(command):
    if "facebook" in command:
        webbrowser.open("https://www.facebook.com")
    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
    elif "twitter" in command:
        webbrowser.open("https://www.twitter.com")
    elif "instagram" in command:
        webbrowser.open("https://www.instagram.com")
    elif "linkedin" in command:
        webbrowser.open("https://www.linkedin.com")
    elif "reddit" in command:
        webbrowser.open("https://www.reddit.com")
    elif "tiktok" in command:
        webbrowser.open("https://www.tiktok.com")
    elif "snapchat" in command:
        webbrowser.open("https://www.snapchat.com")


def process_command(command):
    if command.startswith("open"):
        open_social_media(command)
    elif command == "play news":
        print("playing news")
        speak("playing news")
        play_news()
    elif command.startswith("play"):
        play_music(command)
    else:
        print("Command not recognized. Please try again.")

while True:
    if __name__ == "__main__":
        engine = pyttsx3.init()
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                    print("Initializing Jarvis")
                    print("Listening...")
                    audio = r.listen(source, phrase_time_limit=2)
                    print("Recognizing...")
                    word = r.recognize_google(audio).lower()
                    print("Jarvis thinks you said " + r.recognize_google(audio))
                    if "jarvis" in word:
                         speak("Yes")
                         with sr.Microphone() as source:
                            print("Listening...")
                            r.adjust_for_ambient_noise(source, duration=0.5)
                            audio = r.listen(source)
                            print("Recognizing...")
                            command = r.recognize_google(audio)
                            print(command)
                            process_command(command.lower())
        except Exception as e:
                print(f"Error: {e}")