import pyttsx3
import speech_recognition as sr
from Chats import Chats
from Automations import Calc
from Automations import Time
from Automations import open_app
from Automations import open_website
from Features import GoogleSearch
from Features import TranslateText
from Automations import Music



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

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        audio = r.listen(source)

        try:
            print("\n...")
            query = r.recognize_google(audio, language='en-in')
            print(" ")
            print(f"{query}\n")

        except Exception:

            return ""
        
    query = input("Query : ")
    
    return query.lower()

def TaskExe():
        
    while True:
        
        query = TakeCommand()

        if 'google search' in query:

            GoogleSearch(query)

        elif 'remember' in query:
            
            query = query.replace("remember","")
            

        elif 'calculate' in query:

            query = query.replace("calculate","")
            
            Calc(query)

        elif 'open website' in query:

            query = query.replace("open","")
            query = query.replace("website","")
            query = query.replace(" ","")

            print(f"Opening {query}...")
        
            open_website(f"https://{query}.com")

        elif 'open app' in query:

            query = query.replace("open","")
            query = query.replace("app","")
            query = query.replace(" ","")

            print(f"Opening {query}...")
        
            open_app(query)

        elif 'play music' in query:

            Music(query)

        elif 'time' in query:
                
            Time()

        elif 'translate' in query:

            TranslateText(query, lang='en')
            
        else:

            reply = Chats(query)

            Speak(reply)
        
            if 'bye' in query:

                break

            elif 'exit' in query:

                break
        
            elif 'sleep' in query:

                break


TaskExe()