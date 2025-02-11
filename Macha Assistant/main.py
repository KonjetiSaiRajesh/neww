import pyttsx3
import speech_recognition as sr
import keyboard
import time
import os
import subprocess as sp
import pyautogui

from conv import random_text
from datetime import datetime
from decouple import config
from random import choice
from online import find_my_ip, search_on_google,search_on_wikipedia,youtube 


try:
    engine = pyttsx3.init()
except Exception as e:
    print(f"Failed to initialize pyttsx3: {e}")
    engine = None  # Set engine to None to avoid further issues
if engine is not None:
    engine.setProperty('volume', 1)
    engine.setProperty('rate', 225)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

USER = config('USER')
HOSTNAME = config('BOT')

listening = False
queri = ""  

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def greet_me():
    hour = datetime.now().hour
    if hour >= 6 and hour < 12:
        speak(f"Good morning {USER}")
    elif hour >= 12 and hour < 16:
        speak(f"Good afternoon {USER}")
    elif hour >= 16 and hour < 20:
        speak(f"Good evening {USER}")
    speak(f"I am {HOSTNAME}. How can I assist you, {USER}?")

def start_listening():
    global listening
    listening = True
    print("Started Listening....")

def pause_listening():
    global listening
    listening = False
    print("Stopped Listening....")

keyboard.add_hotkey('ctrl + s', start_listening)
keyboard.add_hotkey('ctrl + p', pause_listening)

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing......")
        queri = r.recognize_google(audio, language='en-in').lower()
        print(f"User said: {queri}")

        if 'stop' in queri or 'exit' in queri:
            hour = datetime.now().hour
            if hour >= 21 or hour < 6:
                speak("Good night, Take care!")
            else:
                speak("Have a nice day!")
            exit()

        elif "how are you" in queri:
            speak("I am absolutely fine, thank you for asking! What about you?")
        
        return queri  

    except sr.UnknownValueError:
        speak("Sorry, I didn't get that. Can you please repeat that?")
        return "none" 

    except sr.RequestError:
        speak("I'm having trouble connecting to the recognition service. Please check your internet connection.")
        return "none"  

if __name__ == "__main__":
    greet_me()
    while True:
        if listening:
            queri = take_command()

            if queri == "none":
                continue  

            if "open command prompt" in queri:
                speak("Opening command prompt")
                os.system('start cmd')

            elif "open camera" in queri:
                speak("Opening camera")
                sp.run('start microsoft.windows.camera:', shell=True)

            elif "open notepad" in queri:  
                speak("Opening Notepad")
                os.startfile("C:\\Windows\\notepad.exe")

            elif "open valorant" in queri:  
                speak("Opening Valorant")
                os.startfile(r"C:\Riot Games\Riot Client\RiotClientServices.exe")

            elif "open uipath" in queri:
                speak("Opening UI Path")
                os.startfile(r"C:\Users\konje\AppData\Local\Programs\UiPath\Studio\UiPath.Studio.exe")

            elif "open zoom" in queri:
                speak("Opening zoom")
                os.startfile(r"C:\Users\konje\AppData\Roaming\Zoom\bin\Zoom.exe")

            elif "open excel" in queri:
                speak("Opening Excel")
                os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk")
            
            elif "open word" in queri:
                speak("Opening Word")
                os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")

            elif "open powerpoint" in queri:
                speak("Opening PowerPoint")
                os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk")

            elif "open outlook" in queri:
                speak("Opening Outlook")
                os.startfile(r"c:\ProgramData\Microsoft\Windows\Start Menu\Programs\Outlook (classic).lnk")

            elif "open chrome" in queri:
                speak("Opening Chrome")
                os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            
            elif "open edge" in queri:
                speak("Open Edge")
                os.startfile(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

            elif "ip address" in queri:
                ip_address = find_my_ip()
                speak(f"Your IP address is: {ip_address}")
                print(f"Your ip address is: {ip_address}")
            
            elif "open youtube" in queri:
                speak("What do you want to see in youtube?")
                video = take_command().lower
                speak("Opening Youtube")
                youtube(video)

            elif "open google" in queri:
                speak("What do you want to search in google?")
                queri = take_command().lower
                speak("Searching in google")
                search_on_google(queri)

            elif "wikipedia" in queri:
                speak("What do you want to search in wikipedia?")
                search = take_command().lower
                results = search_on_wikipedia(search)
                speak(f"According to wikipedia , {results}")
                speak("I am printing results")
                print(results)