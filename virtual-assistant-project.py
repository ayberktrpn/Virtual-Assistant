import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()



#to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=10,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("How are you?")

#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('ayberktirpan@gmail.com', 535)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'your password')
    server.sendmail('your email id', to, content)
    server.close()


if __name__ == "__main__":
    wish()
    while True:
    #if 1:

        query = takecommand().lower()

        #logic building for tasks

        if "open notes" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open google" in query:
            opath = "C:\\Users\\ayber\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
            os.startfile(opath)

        elif "open cmd" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
                cap.release()
                cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "C:\\Users\\ayber\\Music\\music"
            songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))


        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")


        elif "search google" in query:
            speak("what should ı search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            pywhatkit.sendwhatmsg("+9005060508606", "nerde aşı yarramın başı",15,38)

        elif "play song on youtube" in query:
            pywhatkit.playonyt("see you again")

        elif "how are" in query:
            speak(f"I am fine thank you. what can I"
                  f" do for you?")

        elif "time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M")
            speak(f"the time is {strTime}")

        elif "news" in query:
            news = webbrowser.open_new_tab("https://www.haberler.com")
            speak("Here are some news")

        elif "email" in query:
            try:
                speak("what should I say?")
                content = takecommand().lower()
                to = "ayberktirpan@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to ayberk")

            except Exception as e:
                print(e)
                speak("sorry I can't ")

        elif "Who are you" in query:
            speak("I am your virtual assistant.")


        elif "see you" in query:
            speak("I am always here. See you later")
            sys.exit()





