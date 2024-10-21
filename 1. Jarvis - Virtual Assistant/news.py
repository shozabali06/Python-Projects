import requests
from gtts import gTTS
import pygame
import os
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
