import wolframalpha
import pyttsx3
from os import startfile
import os
import webbrowser
import datetime
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep



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

def Time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    Speak(f"The current time is {current_time}")

def WolfRamAlpha(query):
    apikey = "TWWURG-P8VKYEQVP5"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text

        return answer
    
    except:

        Speak("The value is not answerable")

def Calc(query):

    Term = str(query)

    Term = Term.replace("into","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("by","/")
    
    Final = str(Term)

    try:
        result = WolfRamAlpha(Final)

        Speak(result)

    except:
        Speak("The value is not answerable")

def Open(query):

    if 'open' in query:

        name = query.replace("open ","")

        Name = str(name)

        startfile

def open_website(url):

    webbrowser.open(url)

def open_app(app):

    press_and_release('windows')

    sleep(1)

    write(app)

    sleep(1)

    press('enter')

def Music(name):

    name = name.replace("play","")
    name = name.replace("music","")

    press_and_release('windows')

    sleep(1)

    write('music')

    sleep(1)

    press('enter')

    sleep(10)

    click(x=1562, y=77)

    write(name)

    sleep(5)

    click(x=665, y=167)

    sleep(5)

    click(x=125,y=490)

    click(x=125,y=490)