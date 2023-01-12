import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests
import pywhatkit
from gtts import gTTS
from playsound import playsound
from googletrans import Translator

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#speak function


def speak(audio):
    engine.say(audio)
    #rate
    vol=engine.getProperty('volume')
    engine.setProperty('volume',vol+1.5)
    engine.runAndWait()

def wishMe():
    hr = int(datetime.datetime.now().hour)
    if hr>=0 and hr<=12:
        speak("Good Morning!")
    elif hr>=12 and hr<=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hey Darling! How can I help You")

def takecommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("..Listening..")
        r.pause_threshold=0.1
        audio=r.listen(source)
    try:
        print("...Recognising...")
        query=r.recognize_google(audio, language='en-in')
        print(f'User Said: {query}\n')
    except Exception as e:
        print(e)

        print("say that again Please...")
        speak("Sorry!I can't hear you")
        return "none"
    
    return query


def sendEmail(To,msg):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("maheshnallada@gmail.com","M@he$h2002")
    server.sendmail('maheshnallada@gmail.com',To,msg)
    server.close()


if __name__=="__main__":
    wishMe()
    #logic for executing tasks based on query
    while True:
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia!")
            query=query.replace("wikpedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia..")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'command prompt' in query:
            os.system('start cmd')
     

        elif 'play music' in query:
            music_dir="C:\\Users\\MAHESH\\Music"
        
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir, the time is {strtime}')

        elif 'open vs code' in query:
            Path="C:\\Users\\MAHESH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(Path)

        #sending email
        elif 'email to vijay' in query:
            try:
                speak("What Should i send as a message")
                content=takecommand()
                to="kvijayasunilkumar@gmail.com"
                sendEmail(to,content)
                speak("Email has been be sent!")
            except Exception as e:
                print(e)
                speak("sorry")

        #ip address
        elif 'ip address' in query:
            ip=requests.get(" https://api64.ipify.org/?format=json").json()
            speak("Here is You Ip address!")
            print(ip["ip"])
            speak(ip["ip"])

        #playing video on youtube
        elif "video on youtube" in query:
            speak("What do you want to play on youtube")
            video=takecommand().lower()
            pywhatkit.playonyt(video)
        
        #search on google
        elif 'search on google' in query:
            speak("What do you want to search?")
            x=takecommand().lower()
            pywhatkit.search(x)

        #sending whatsapp message
        elif 'whatsapp message' in query:
            '''
            speak("Please tell me the number")
            num=takecommand()
            str1=""
            print(type(num))
            for i in str(num).strip():
                if " " not in str1:
                    str1+=i
            num=int(str1)
            print(num,type(num))
            '''
            num=7569335811
            speak("Please Tell me the message to be sent!")
            msg=takecommand()
            pywhatkit.sendwhatmsg(f"+91{int(num)}",msg.lower(),21,54)
            speak("message sent successfully")

        #random joke
        elif 'joke' in query:
            header={"Accept":'application/json'}
            result=requests.get("https://icanhazdadjoke.com/",headers=header).json()
            speak("Hope You will like this joke sir!")
            joke=result['joke']
            print(joke)
            speak(joke)

        #advice
        elif 'advice' in query:
            adv=requests.get("https://api.adviceslip.com/advice").json()
            speak("Here is an advice for you sir!")
            x=adv['slip']['advice']
            print(x)
            speak(x)

        #translate

        elif 'good bye' or 'goodbye' in query:
            speak("Thank you! Have a Nice day...")
            break



