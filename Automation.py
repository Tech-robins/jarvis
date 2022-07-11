from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import press_and_release  
from keyboard import write
from time import sleep
from datetime import datetime
import pyttsx3
import speech_recognition as sr
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import webbrowser as web
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',170)

def Speak(audio):
    print("   ")
    print(f": {audio} ")
    print("   ")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(": Listening...")

        r.pause_threshold = 1

        audio = r.listen(source)

    try:
        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": your command : {query}\n")

    except:
        return ""
       
    return query.lower()             

def WhatsappMsg(name,message):
     
    startfile("https://web.whatsapp.com/")

    sleep(10)

    click(x=239, y=253)

    sleep(3)

    write(name)

    sleep(2)

    click(x=168, y=430)

    sleep(1)

    click(x=798, y=1015)

    sleep(1)

    write(message)

    press('enter')

def WhatsappCall(name):

    startfile("https://web.whatsapp.com/")

    sleep(10)

    click(x=193, y=253)

    sleep(1)

    write(name)

    sleep(1)

    click(x=304, y=415)

    sleep(1)

    click(x=798, y=1015)

    sleep(1)

    click(x=1198, y=63) 

def WhatsappChat(name):

    startfile("https://web.whatsapp.com/")

    sleep(10)

    click(x=193, y=253)

    sleep(1)

    write(name)

    sleep(1)

    click(x=304, y=415)

    sleep(1)

    click(x=798, y=1015)

    sleep(1)        

def ChromeAuto(command):

    query = str(command)

    if 'new tab' in query:
        press_and_release('Ctrl + t')

    elif 'close tab' in query:
        press_and_release('Ctrl + w')

    elif 'new window' in query:
        press_and_release('Ctrl + n')

    elif 'history' in query:
        press_and_release('Ctrl + h')

    elif 'download' in query:
        press_and_release('Ctrl + j')

    elif 'bookmark' in query:
        press_and_release('Ctrl + b')
        press('enter')

    elif 'incognito' in query:
        press_and_release('Ctrl + Shift + n')

    elif 'switch tab' in query:

        tab = query.replace("switch tab", "")
        Tab = tab.replace("to", "")
        
        num = Tab
        bb = f'Ctrl + {num}'
        press_and_release(bb)
        
    elif 'open' in query:
        name = query.replace("open", "")
        NameA = str(name)

        if 'youtube' in NameA:
            web.open("https://www.youtube.com/")
    
        elif 'instagram' in NameA:
            web.open("https://www.instagram.com/")

        elif 'facebook' in NameA:
            web.open("https://www.facebook.com/")

    else:
        string = "https://www." + NameA + ".com"
        string_2 = string.replace(" ", "")
        web.open(string_2)
       
def YouTubeAuto(command):   

    query = str(command)

    if 'pause' in query:
        press('space bar')

    elif 'resume' in query:
        press('space bar')

    elif 'full screen' in query:
        press('f')

    elif 'film screen' in query:
        press('t')

    elif 'skip' in query:
        press('1')

    elif 'back' in query:
        press('j')

    elif 'increase' in query:
        press_and_release('SHIFT+ .')

    elif 'decrease' in query:
        press_and_release('SHIFT + ,')

    elif 'previous' in query:
        press_and_release('SHIFT + p')

    elif 'next' in query:
        press_and_release('SHIFT + n')

    elif 'mute' in query:
        press('m')

    elif 'unmute' in query:
        press('m')

    elif 'search' in query:
        click(x=607, y=161)

        Speak('what to search sir')

        search = TakeCommand()

        write(search)

        sleep(1)

        press('Enter')

    else:
        Speak("No Command Found!")

def GoogleMaps(Place):

    Url_Place = "https://www.google.com/maps/place/" + str(Place)

    geolocator = Nominatim(user_agent="myGeocoder")

    location = geolocator.geocode(Place , addressdetails= True)

    target_latlon = location.latitude , location.longitude

    web.open(url=Url_Place)

    location = location.raw['address']

    target = {'city' : location.get('city',''),
                'state' : location.get('state',''),
                'country' : location.get('country','')}

    current_loca = geocoder.ip('me')

    current_latlon = current_loca.latlng

    distance = str(great_circle(current_latlon,target_latlon))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)


    Speak(target)
    Speak(f"Sir , {Place} iS {distance} Kilometre Away From Your Location . ")

def Notepad():

    Speak("Tell Me The Query .")
    Speak("I Am Ready To Write .")

    writes = TakeCommand()

    time = datetime.now().strftime("%H:%M")

    filename = str(time).replace(":","-") + "-note.txt"

    with open(filename,"w") as file:

        file.write(writes)

    path_1 = "P:\\AI Asisstant\\" + str(filename)

    path_2 = "P:\\AI Asisstant\\Database\\NotePad\\" + str(filename)

    os.rename(path_1,path_2)

    os.startfile(path_2)

def CloseNotepad():

    os.system("TASKKILL /F /im Notepad.exe")

