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

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[1].id)


class jarvis_code():

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
                path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
                self.speak("opening notepad")
                os.startfile(path)

            # openiong the google chrome
            elif "open google" in query:
                path = "C:\\ProgramData\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome"
                self.speak("what do you want to search on google sir")
                search = self.take_command().lower()
                self.speak("opening google")
                webbrowser.open(search)

            # opening command prompt
            elif "open command prompt" in query:
                self.speak("opening command prompt")
                os.system("start cmd")

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
                print("searching wikipedia.....")
                self.speak("searching wikipedia")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                print(results)
                self.speak("according to wikipedia")
                self.speak(results)

            # opening youtube
            elif "open youtube" in query:
                self.speak("opening youtube")
                webbrowser.open("www.youtube.com")

            # opening facebook
            elif "open facebook" in query:
                self.speak("opening facebook")
                webbrowser.open("https://www.facebook.com/")

            # opening instagrasm
            elif "open instagram" in query:
                self.speak("opening instagram")
                webbrowser.open("https://www.instagram.com/")

            # opening linkedin
            elif "open linkedin" in query:
                self.speak("opening linkedin")
                webbrowser.open(
                    "https://www.linkedin.com/feed/?trk=guest_homepage-basic_nav-header-signin")

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
            
            #saying the jokes
            elif "joke" in query :
                joke = pyjokes.get_joke()
                self.speak(joke)  

jarvis = jarvis_code()
# jarvis.speak("hello sir how can i help you")
while True:
    query = jarvis.take_command()
    if None == query:
        pass
    elif "wake up jarvis" in query:
        jarvis.wish()
        # query = jarvis.take_command()
        jarvis.desire()

# this is for testing
