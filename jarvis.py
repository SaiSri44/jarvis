import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import pyautogui
import time
import PyPDF2
import pytube

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[1].id)


class social_media():
    def open_facebook(self):
        webbrowser.open("https://www.facebook.com/")

    def open_instagram(self):
        webbrowser.open("https://www.instagram.com/")

    def open_linkedin(self):
        webbrowser.open(
            "https://www.linkedin.com/feed/?trk=guest_homepage-basic_nav-header-signin")


class system_apps():
    def speak(self, audio):
        engine.say(audio)
        engine.runAndWait()

    def open_notepad(self):
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
        os.startfile(path)

    def open_google(self):
        path = "C:\\ProgramData\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome"
        path = "C:\\ProgramData\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome"
        self.speak("what do you want to search on google sir")
        search = self.take_command().lower()
        self.speak("opening google")
        webbrowser.open(search)

    def open_command_prompt(self):
        self.speak("opening command prompt")
        os.system("start cmd")


class jarvis_abilites():
    def speak(self, audio):
        engine.say(audio)
        engine.runAndWait()

    def taking_screen_shot(self):
        print("sir,please tell me the name of this screenshot file")
        self.speak("sir,please tell me the name of this screenshot file")
        name = self.take_command().lower()
        print("Hang on for few seconds sir , I am taking the screenshot")
        self.speak("Hang on for few seconds sir , I am taking the screenshot")
        time.sleep(3)
        img = pyautogui.screenshot()
        img.save(f"{name}.jpg")
        print("ok sir i am done with taking screenshot,it is saved in our current folder,i am ready for another command sir")
        self.speak(
            "ok sir i am done with taking screenshot, it is saved in our current folder, i am ready for another command sir")

    def audio_book(self):
        # note: book should be in this dorectory,or you can enter the location of book in open commmand 
        book = open("electrical textbook.pdf",'rb') 
        # opening the book in binary mode
        pdfreader = PyPDF2.PdfFileReader(book)
        # intilaising the reader,creating the object of the module
        pages = pdfreader.numPages
        # getting total no of pages
        self.speak(f"This book consists of {pages} pages")
        self.speak("sir,please say which page i should read")
        self.speak("Enter the page number")
        # getting the page no to which we should read
        page_no = int(input("Enter the page no : ")) 
        print(page_no)
        # getting the page
        page = pdfreader.getPage(page_no)
        # extracting the text from the page
        text = page.extractText()
        print(text) 
        self.speak(text) 

    def find_location(self) :
            try :
                ip = get("https://api.ipify.org").text
                print(ip)
                url = "https://get.geojs.io/vl/ip/geo/" + ip+".json"
                # url to get the location
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # it will give data in the form of dictonary
                city = geo_data['city'] 
                # it mnay throw error sometimws because there may be no state for some plcaes like delhi
                state = geo_data['state'] 
                country = geo_data['country']
                self.speak(f"Sir we are in {city} city in {state} state of {country}") 
            except :
                self.speak("Sorry sir,due to poor internet i cannot find the location")
                # finding location takes more time ,so we added exception.
                pass 

    def youtube_video_download(self) :
        self.speak("sir, please enter the youtube video url")
        link = input("Enter the video url ")
        video = pytube.YouTube(link) 
        stream = video.streams.get_highest_resolution()
        self.speak("hang on sir,video is downloading in current folder")  
        stream.download()
        self.speak("ok sir,youtube video is downloaded ,you may proceed further") 

    def search_wikipedia(self,query) :
        print("searching wikipedia.....")
        self.speak("searching wikipedia")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        print(results)
        self.speak("according to wikipedia")
        self.speak(results)
           

class jarvis_code(social_media,system_apps,jarvis_abilites):

    def speak(self, audio):
        engine.say(audio)
        engine.runAndWait()

    def take_command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            audio = r.listen(source, timeout=1, phrase_time_limit=5)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(query)
        except:
            return None
        return query.lower()

    def wish(self):
        hour = int(datetime.datetime.now().hour)
        minute = int(datetime.datetime.now().minute)
        if hour >= 0 and hour <= 12:
            self.speak(f"Good morning ,it's {hour} {minute} am")
            print(f"Good morning ,it's {hour} : {minute} A.M")
        elif hour > 12 and hour <= 18:
            self.speak(f"Good Afternoon,it's {hour-12} {minute} pm")
            print(f"Good afternoon ,it's {hour-12} : {minute} P.M") 
        else:
            self.speak(f"Good Evening,it's {hour-12}  {minute} pm") 
            print(f"Good evening,it's {hour-12} : {minute} P.M") 
        self.speak("Hii Sir, I am jarvis, please tell how can i help you")
          

    def desire(self):
        while True:
            # opening the system apps
            # opening notebook
            query = self.take_command()
            if query == None:
                pass
            elif "open notepad" in query:
                 self.speak("opening notepad")
                 self.open_notepad()

            # openiong the google chrome
            elif "open google" in query:
                self.open_google() 

            # opening command prompt
            elif "open command prompt" in query:
                self.open_command_prompt()

            # playing the music
            elif "play music" in query:
                music_directory = "E:\\Music\\english"
                songs = os.listdir(music_directory)
                random.shuffle(songs)
                for song in songs:
                    if song.endswith(".mp3"):
                        os.startfile("E:\\Music\\english\\"+song)

            # getting ip address
            elif "ip address" in query:
                ip = get("https://api.ipify.org").text
                print(ip)
                self.speak(f"sir your ip address is {ip}")

            # performing the online tasks

            # searching for something in wikipedia
            elif "wikipedia" in query:
                self.search_wikipedia(query)

            # opening youtube
            elif "open youtube" in query:
                self.speak("opening youtube")
                webbrowser.open("www.youtube.com")

            # opening facebook
            elif "open facebook" in query:
                self.speak("opening facebook") 
                self.open_facebook() 

            # opening instagrasm
            elif "open instagram" in query:
                self.speak("opening instagram")
                self.open_instagram()
                
            # opening linkedin
            elif "open linkedin" in query:
                self.speak("opening linkedin")
                self.open_linkedin()
                
            # sending whatsapp message with jarvis
            elif "send whatsapp message" in query:
                kit.sendwhatmsg("+918688136687",
                                "this message is sent by jarvis", 6, 9)
                self.speak("Whatsapp meassage sent succcesfullly")

            # playing song on youtube
            elif "play songs on youtube" in query:
                self.speak("playing songs on youtube")
                kit.playonyt("never lie to me")

            # making jarvis to go to sleep
            elif "go to sleep" in query:
                self.speak(
                    "Ok sir i am going to sleep,you can call me anytime")
                break

            # terminating the programm execution
            elif "stop" in query:
                self.speak("Thank you sir for using me,have a nice day")
                sys.exit()

            # shutdowning the sysytem
            elif "shutdown" in query:
                self.speak("Got it Sir, shutdowning the Pc,")
                self.speak("Thank you Sir,Have a nice day")
                os.system("shutdown /s /t 5")

            # restarting the computer
            elif "restart" in query:
                self.speak("Hang on Sir, restarting the Pc")
                os.system("shutdown /r /t 5")
            
            # saying the jokes
            elif "joke" in query :
                joke = pyjokes.get_joke()
                self.speak(joke) 

            # finding the location
            elif "where i am " in query or "location" in query :
                 self.find_location()

             # taking the screenshot
            elif "take screenshot" in query or "screenshot" in query :
                   self.taking_screen_shot()

            #reading the pdf       
            elif "read book" in query :
                   self.audio_book()

             # downloading the youtube video   
            elif "download youtube" in query or "download" in query :
                self.youtube_video_download() 
                
jarvis = jarvis_code()
# jarvis.speak("hello sir how can i help you")
while True:
    query = jarvis.take_command()
    if None == query:
        pass
    elif "hello jarvis" in query:
        jarvis.wish()
        # query = jarvis.take_command()
        jarvis.desire()

# this is for testing





