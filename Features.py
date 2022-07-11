import pywhatkit
import wikipedia
from pywikihow import WikiHow, search_wikihow
import os
import pyttsx3
import webbrowser as web
import wolframalpha



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

def GoogleSearch(term):

    query = term.replace("jarvis","")
    query = query.replace("what is","")
    query = query.replace("how are","")
    query = query.replace("how to","")
    query = query.replace("what do you mean by","")
    writeab = str(query)

    oooooo = open('P:\\AI Asisstant\\Data.txt','a')
    oooooo.write(writeab)
    oooooo.close()
    
    Query = str(query)

    pywhatkit.search(Query)

    os.startfile('P:\\AI Asisstant\\Extraprogram\\Alarm.py')

    if 'how to' in Query:

        max_result = 1

        how_to_func = search_wikihow(query=Query,max_results=max_result)

        assert len(how_to_func) == 1

        how_to_func[0].print()

        Main.Speak(how_to_func[0].summary)
        
    else:   
        search = wikipedia.summary(Query,1)
        Main.Speak(f": Acooring to Your Search : {search}")    

def YouTubeSearch(term):
        result = "https://www.youtube.com/results?search_query=" + term
        web.open(result)
        Speak("This Is What I Found For Your Search .")
        pywhatkit.playonyt(term)
        Speak("This May Also Help You Sir .")    

def Alarm(query):

    TimeHere=  open('P:\\AI Asisstant\\Data.txt','a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("P:\\AI Asisstant\\Extraprogram\\Alarm.py")        

def DownloadYouTube():

    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip
    from time import sleep

    sleep(2)
    click(x=759,y=954)
    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value) # Important 

    def Download(link):


        url = YouTube(link)


        video = url.streams.first()


        video.download('P:\\AI Asisstant\\Database\\Youtube')


    Download(Link)


    Speak("Done Sir , I Have Downloaded The Video .")

    Speak("You Can Go And Check It Out.")


    os.startfile('P:\\AI Asisstant\\Database\\Youtube')

def Speedtest():
    os.startfile("P:\\AI Asisstant\\Database\\New folder\\SpeedTestGui.py")  

def WolfRam(query):

    api_key = "LH3A93-AUXU4AVKYP"

    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)
    
    try:
        Answer = next(requested.results).text
        return Answer

    except:

        Speak("An string Value  is not Answerable. ")      

def Calculator(query):
    Term = str(query)

    Term = Term.replace("jarvis","")
    Term = Term.replace("add","+")
    Term = Term.replace("into","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")
    Term = Term.replace("multiply","*")

    Final = str(Term)

    try:
        result = WolfRam(Final)
        Speak(F"{result}")

    except:
        Speak("An string Value  is not Answerable. ")

def Temp(query):
    Term = str(query)

    Term = Term.replace("jarvis","")
    Term = Term.replace("temperature","")
    Term = Term.replace("in","")
    Term = Term.replace("what is the","")
    Term = Term.replace("now","")

    temp_query = str(Term)

    if 'outside' in temp_query:
        var1 = "Temperature in meerut"

        answer = WolfRam(var1)

        Speak(f"{var1} is {answer} .")

    else:
        var2 =  "temperature In " + temp_query

        answ = WolfRam(var2)

        Speak(f"{var2} Is {answ}")

def DateConverter(Query):

    Date = Query.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")
    return str(Date)

def My_Location():

    op = "https://www.google.com/maps/place/Delhi/@28.6472799,76.8130619,83757m/data=!3m2!1e3!4b1!4m5!3m4!1s0x390cfd5b347eb62d:0x37205b715389640!8m2!3d28.7040592!4d77.1024902"

    Speak("Checking....")

    web.open(op)

    ip_add = requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_q = requests.get(url)

    geo_d = geo_q.json()

    state = geo_d['city']

    country = geo_d['country']

    Speak(f"Sir , You Are Now In {state , country} .")
