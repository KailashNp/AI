from multiprocessing.pool import TERMINATE
import pyttsx3
import speech_recognition as sr
import datetime
import os
import subprocess
import webbrowser as wb
import pyautogui
import pywhatkit
import wikipedia
import pyjokes
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import sys
from clap import Tester

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)
voicespeed = 140
engine.setProperty('rate', voicespeed)
chrome_path = '"C:/Program Files/Google/Chrome/Application/chrome.exe" %s'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-us')
    except Exception as e:
        print(e)
        return "---"
    return query


def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)
    print(time)


def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("morning!")

    elif hour >= 12 and hour < 18:
        speak("good afternoon !")

    else:
        speak("good evening")

    speak(" initiating system......                              loading vikraant                ")
    speak(
        "..................................       i am VIKRAANT.      Your personal assistant.   What can i do for "
        "you sir?")


def open_chrome():
    url = 'www.google.com'
    wb.get(chrome_path).open(url)


def open_wa():
    uql = "https://web.whatsapp.com/"
    wb.get(chrome_path).open(uql)


def open_ig():
    uml = "https://www.instagram.com/"
    wb.get(chrome_path).open(uml)


def open_gmail():
    uuvl = "https://www.mail.google.com/"
    wb.get(chrome_path).open(uuvl)


def open_song():
    song = query.replace('play', '')
    speak('playing ' + song)
    pywhatkit.playonyt(song)


def open_amaz():
    anal = "https://www.amazon.in/"
    wb.get(chrome_path).open(anal)


def open_fk():
    fk = "https://www.flipkart.com/"
    wb.get(chrome_path).open(fk)


def open_youtube():
    ulr = 'https://www.youtube.com/'
    wb.get(chrome_path).open(ulr)


def open_twitter():
    uurl = 'https://twitter.com/home'
    wb.get(chrome_path).open(uurl)


def open_rickroll():
    urel = 'https://youtu.be/dQw4w9WgXcQ'
    wb.get(chrome_path).open(urel)


def open_maranamass():
    uhel = 'https://youtu.be/88iypMO9H7g'
    wb.get(chrome_path).open(uhel)


def open_trending():
    usel = 'https://www.youtube.com/feed/trending'
    wb.get(chrome_path).open(usel)


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()

        if "date" in query:
            date()

        if "open chrome" in query:
            speak('Ok Sir')
            open_chrome()

        elif "open youtube" in query:
            speak('Ok Sir')
            open_youtube()

        elif 'open twitter' in query:
            speak('Ok Sir')
            open_twitter()
        elif "wake up" in query:
            speak("Always up and ready for you ")

        elif 'who are you' in query:
            speak('I am VIKRAANT.   Your personal assistant')

        elif "what is your name" in query:
            speak("my name is VIKRAANT. Your personal assistant")

        elif "are you like google assistant" in query:
            speak("The basis of me may look like google assistant. but   i can do a lot of things that google assisant cannot do")


        elif 'amazon' in query:
            speak('Ok Sir')
            open_amaz()
            speak("you do no have any orders right now")


        elif 'flipkart' in query:
            speak("opening flipkart")
            open_fk()

        elif 'marana mass' in query:
            speak('Ok Sir')
            open_maranamass()

        elif 'trending' in query:
            speak('Trending now......')
            open_trending()

        elif 'play' in query:
            open_song()

        elif "instagram" in query:
            speak("Ok sir checking instagram")
            open_ig()

        elif "mail" in query:
            speak("opening gmail sir")
            open_gmail()

        elif 'open spotify' in query:
            speak('ok sir      opening spotify')


        elif "what is my ip address" in query:
            speak("Checking")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                speak("your ip adress is")
                speak(ipAdd)
            except Exception as e:
                speak("network is weak, please try again some time later")

        elif "who created you" in query:
            speak("I was created by  Tharun,  Nikhil,  Kailash . I am made with python language.")

        elif 'type' in query:
            query = query.replace("type", "")
            pyautogui.write(f"{query}")

        elif 'google search' in query:
            query = query.replace("google search", "")
            pyautogui.hotkey('alt', 'd')
            pyautogui.write(f"{query}", 0.1)
            pyautogui.press('enter')


        elif 'previous tab' in query:
            pyautogui.hotkey('ctrl', 'shift', 'tab')
        elif 'next tab' in query:
            pyautogui.hotkey('ctrl', 'tab')
        elif 'close tab' in query:
            pyautogui.hotkey('ctrl', 'w')
        elif "rick roll" in query:
            open_rickroll()

        elif 'dai' in query:
            speak("Shut up ")

        elif "Lock the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "logout" in query:
            pyautogui.hotkey('winleft', 'l')

        elif "go to sleep" in query:
            speak(' alright then, I am switching off')
            sys.exit()

        elif "open pycharm" in query:
            speak("opening pycharm")
            location = "C:\Program Files\JetBrains\PyCharm Community Edition 2021.3.3\bin\pycharm64.exe"
            pycharm = subprocess.Popen(location)

        elif "who is tarun" in query:
            speak("He is one of my developers. He is a passionate programmer.")
        elif "who is nikhil" in query:
            speak(" he is one of my developers.A very good programmer")
        elif "who is kailash" in query:
            speak("Aspiring programmer. He is one of my developers")

        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
            print(result)
        elif "whatsapp" in query:
            speak("opening whatsapp")

        elif "temperature" in query:
            search = "temperature in chennai"
            url = f"https://www.google.com//search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif "change window" in query:
            speak("ok sir")
            pyautogui.hotkey('alt', 'tab')

        elif "open folder" in query:
            pyautogui.hotkey("winleft", "e")

        elif "any change in code" in query:
            speak("do not worry sir, i updated myself last night")


        elif "volume up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
        elif "volume down" in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
        elif "mute" in query:
            pyautogui.press("volumemute")


        elif "search" in query:
            speak("what should i search?")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")



        elif "open notepad" in query:
            speak("opening notepad")
            location = "C:/WINDOWS/system32/notepad.exe"
            notepad = subprocess.Popen(location)

        elif "close notepad" in query:
            speak("closing notepad")
            notepad.terminate()

        elif "joke" in query:
            speak(pyjokes.get_jokes())
        elif "who is pee" in query:
            speak("pee    pee    pee   pee ")


        elif "log out" in query:
            speak('logging out in 5 second')
            sleep(5)
            os.system("shutdown - l")

        elif "shutdown" in query:
            speak('shutting down in 5 second')
            sleep(5)
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            speak('initiating restart in 5 second')
            sleep(5)
            os.system("shutdown /r /t 1")



        elif "hidden menu" in query:

            pyautogui.hotkey('winleft', 'x')

        elif "close this tab" in query:
            pyautogui.hotkey('ctrl', 'w')

        elif "task manager" in query:

            pyautogui.hotkey('ctrl', 'shift', 'esc')

        elif "task view" in query:

            pyautogui.hotkey('winleft', 'tab')

        elif "new tab" in query:
            pyautogui.hotkey('ctrl', 't')

        elif "new window" in query:
            pyautogui.hotkey('ctrl', 'n')

        elif "run window" in query:
            pyautogui.hotkey('winleft', 'r')

        elif "change to tab one" in query:
            pyautogui.hotkey('ctrl', '1')

        elif "select all" in query:
            pyautogui.hotkey('ctrl', 'a')
        elif "go to the next line" or "enter" in query:
            pyautogui.press("enter")

        elif "snip" in query:
            pyautogui.hotkey('winleft', 'shift', 's')

        elif "close this app" in query:

            pyautogui.hotkey('alt', 'f4')

        elif "setting" in query:

            pyautogui.hotkey('winleft', 'i')

        elif "new virtual desktop" in query:

            pyautogui.hotkey('winleft', 'ctrl', 'd')

        elif "stop" in query:
            speak("Ok sir")
            break
        elif "bye" in query:
            speak("Bye")
            break
        elif "see you later" in query:
            speak("See you later, Bye")
            break
