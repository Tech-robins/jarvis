import requests
from datetime import datetime
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import os
from PIL import Image
import pyttsx3
import random
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

Api_Key = "PdUeFeTBlPyMQcRw1J0oGcNXCaBOazQ5xWW2WwSz"

def NasaNews(Date):

    Speak("Extracting Data From Nasa . ")

    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)

    Params = {'date':str(Date)}
    
    r = requests.get(Url,params = Params)

    Data = r.json()

    Info = Data['explanation']

    Title = Data['title']

    print(Title)
    
    Image_Url = Data['url']

    Image_r = requests.get(Image_Url)

    FileName = str(Date) + '.jpg'

    with open(FileName,'wb') as f:

        f.write(Image_r.content)

    Path_1 = "P:\\AI Asisstant\\" + str(FileName)
    Path_2 = "P:\\AI Asisstant\\Database\\NasaDatabase\\" + str(FileName)

    os.rename(Path_1, Path_2)

    img = Image.open(Path_2)

    img.show()

    Speak(f"Title : {Title}")
    Speak(f"According To Nasa : {Info}")

def Summary(Boby):

    list__ = ('1','2','3','4','5','6')

    value = random.choice(list__)

    path = "P:\\AI Asisstant\\Database\\NasaDatabase\\imageUsed\\" + str(value) + ".jpg"

    os.startfile(path)

    name = str(Boby)

    url = "http://hubblesite.org/api/v3/images" + str(name)

    r = requests.get(url)

    Data = r.json()

    if len(Data) != 0:

        retur =  Data['definition']

        Speak(f"According To The Nasa : {retur}")

    else:

        Speak("No Data Available , Try Again Later!")
    
def MarsImage():

    name = 'curiosity' 

    date = '2020-12-3'

    Api_ = str(Api_Key)

    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={Api_}"

    r = requests.get(url)

    Data = r.json()

    Photos = Data['photos'][:20]

    try:

        for index , photo in enumerate(Photos):

            camera = photo['camera']

            rover = photo['rover']

            rover_name = rover['name']

            camera_name = camera['name']

            full_camera_name = camera['full_name']

            date_of_photo = photo['earth_date']

            img_url = photo['img_src']

            p = requests.get(img_url)

            img = f'{index}.jpg'

            with open(img,'wb') as file:
                file.write(p.content)

            Path_1 = "P:\\AI Asisstant\\" + str(img)

            Path_2 = "P:\\AI Asisstant\\Database\\NasaDatabase\\MarsImage\\" + str(img)

            os.rename(Path_1,Path_2)

            os.startfile(Path_2)

            Speak(f"This Image Was Captured With : {full_camera_name}")

            Speak(f"This Image Was Captured On : {date_of_photo}")

    except:
        Speak("There is An Error!")


