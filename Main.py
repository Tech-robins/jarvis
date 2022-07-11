#Import Important Lib 
from Automation import TakeCommand
import pyttsx3
from playsound import playsound
import speech_recognition as sr
import webbrowser as web
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
from JarvisUI import Ui_MainWindow

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


# def Speak_Assis(audio):
#     kk = gTTS(audio)
#     kk.save('Assis.mp3')
#     playsound('Assis.mp3')

class MainThread(QThread):
    def __init__(self) -> None:
        super(MainThread,self).__init__()

    def run(self):
         self.TaskExe()

    def TakeCommand(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print(": Listening...")

            r.pause_threshold =1

            audio = r.listen(source)
            
        try:
            print(": Recognizing...")

            query = r.recognize_google(audio,language='en-in')

            print(f": your command : {query}\n")

        except:
            return ""
        
        return query.lower()      

    def TaskExe(self):

        while True:

            self.query = self.TakeCommand()

            if 'search' in self.query:
                from Features import GoogleSearch
                GoogleSearch(self.query)
            
            elif 'youtube search' in self.query:
                Query = self.query.replace("jarvis","")
                query = Query.replace("youtube search","")
                from Features import YouTubeSearch
                YouTubeSearch(query)

            elif 'set alarm' in self.query:
                from Features import Alarm
                Alarm(query)

            elif 'download' in self.query:
                from Features import DownloadYouTube
                DownloadYouTube()
                
            elif 'speed test' in self.query:
                from Features import Speedtest
                Speedtest()

            elif 'temperature' in self.query:

                from Features import Temp
                Temp(self.query)

            elif 'whatsapp message' in self.query:

                name = self.query.replace("whatsapp message","")
                name = name.replace("send message","")
                name = name.replace("to", "")
                Name = str(name)
                Speak("whats the message  for {Name}")
                MSG = TakeCommand()
                from Automation import WhatsappMsg
                WhatsappMsg(Name,MSG)

            elif 'call' in self.query:
                from Automation import WhatsappCall
                name = query.replace("call", "")
                name = name.replace("jarvis", "")
                Name = str(name)
                WhatsappCall(Name)

            elif 'so chat' in self.query:
                Speak("with whom ?")
                name = TakeCommand()
                from Automation import WhatsappChat
                WhatsappChat(name)
            
            elif 'new tab' in self.query:
                press_and_release('Ctrl + t')

            elif 'close tab' in self.query:
                press_and_release('Ctrl + w')

            elif 'new window' in self.query:
                press_and_release('Ctrl + n')

            elif 'history' in self.query:
                press_and_release('Ctrl + h')

            elif 'download' in self.query:
                press_and_release('Ctrl + j')

            elif 'bookmark' in self.query:
                press_and_release('Ctrl + b')
                press('enter')

            elif 'incognito' in self.query:
                press_and_release('Ctrl + Shift + n')

            elif 'switch tab' in self.query:

                tab = query.replace("switch tab", "")
                Tab = tab.replace("to", "")
                
                num = Tab
                bb = f'Ctrl + {num}'
                press_and_release(bb)
                
            elif 'open' in self.query:
                name = self.query.replace("open", "")
                NameA = str(name)
                if 'youtube' in NameA:
                    web.open("https://www.youtube.com/")
                elif 'facebook' in NameA:
                    web.open("https://www.facebook.com/")
            
            elif 'youtube' in self.query:

                from Automation import YouTubeAuto
                YouTubeAuto(self.query)

                if 'pause' in self.query:
                    press('space bar')

                elif 'resume' in self.query:
                    press('space bar')

                elif 'full screen' in self.query:
                   press('f')

                elif 'film screen' in self.query:
                    press('t')

                elif 'skip' in self.query:
                    press('1')

                elif 'back' in self.query:
                    press('j')

                elif 'increase' in self.query:
                    press_and_release('SHIFT+ .')

                elif 'decrease' in self.query:
                    press_and_release('SHIFT + ,')

                elif 'previous' in self.query:
                    press_and_release('SHIFT + p')

                elif 'next' in self.query:
                    press_and_release('SHIFT + n')

                elif 'mute' in self.query:
                    press('m')

                elif 'unmute' in self.query:
                    press('m')

                elif 'search' in self.query:
                    click(x=607, y=161)

                    Speak('what to search sir')

                    search = TakeCommand()

                    write(search)

                    sleep(1)

                    press('Enter')

            elif 'space news' in self.query:
                Speak("TEll Me The Date For News .")
                Date = TakeCommand()

                from Features import DateConverter
                Value = DateConverter(Date)

                from Nasa_Api import NasaNews
                NasaNews(Value)
            
            elif 'about' in self.query:
                from Nasa_Api import Summary
                query = query.replace("jarvis ","")
                query = query.replace("about ","")
                Summary(query)

            elif 'mars images' in self.query:

                from Nasa_Api import MarsImage

                MarsImage()

            elif 'where is' in self.query:
                from Automation import GoogleMaps
                Place = query.replace("where is","")
                place = place.replace("jarvis", "")
                GoogleMaps(Place)

            elif 'write a note' in self.query:

                from Automation import Notepad

                Notepad()

            elif 'dismiss' in self.query:

                from Automation import CloseNotepad

                CloseNotepad()

            else:

                from Database.Chatbot.chatbots import ChatterBot

                reply = ChatterBot(self.query)

                Speak(reply)

                if 'bye' in self.query:

                    break

                elif 'exit' in self.query:

                    break

                elif 'go' in self.query:

                    break
    
#--------GUI interface dode------
startExecution = MainThread()  

class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("G.U.I. Material/B.G/1.gif")
        self.ui.Gif1.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("G.U.I. Material/VoiceReg/Siri_1.gif")
        self.ui.Gif2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("G.U.I. Material/ExtraGui/initial.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time= current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)



app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())



        
              

      


