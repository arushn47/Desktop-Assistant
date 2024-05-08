import pywhatkit
import wikipedia
from pywikihow import RandomHowTo, search_wikihow
import os
import speech_recognition as sr
import webbrowser
import pyttsx3
from time import sleep
from googletrans import Translator



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 140)


def Speak(audio):
    print(" ")
    print(f"{audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def GoogleSearch(query):

    query = query.replace("google","")
    query = query.replace("search","")
    query = query.replace("what is","")
    query = query.replace("how to","")
    query = query.replace("who is","")
    query = query.replace("what do you mean by","")
    
    search = f"https://www.google.com/search?q={query}"
    webbrowser.open(search)

    result_page = wikipedia.search(query)
    result = wikipedia.summary(result_page,2)

    Speak(f": According To Your Search : {result}")


def TranslateText(query, lang='en'):
    
    query = query.replace("translate","")
    query = query.replace(" ","")

    translator = Translator()
    translated_text = translator.translate(query, dest=lang)
    Speak(f"The Translated text is {translated_text.text}")

