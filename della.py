import code
from email.mime import audio
from http import server
from unittest import result
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib








# sapi5 is a windows api used to provide inbuid voices voices 
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<17:
        speak("good afternoon")
    else:
        speak("good evening")
        
    speak(" I am della, your personal voice assistant, how may i help you?")


def takeCommand():
    # takes microphone input and gives output a string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print ("Recognizing......")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print("Sorry i couldnot hear you , say taht again please")
        return "None"  
    return query


def sendEmail(to, content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('smcofficialt2022@gmail.com','testaccount2022')
    server.sendmail('smcofficialt2022@gmail.com',to,content)
    server.close()

    

   


if __name__== "__main__":

    wishMe()
    while(True):
        query=takeCommand().lower()
    #  logic for demonstating commands  
        if 'wikipedia' in query:
            speak("searching wikipedia....")
            query= query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir= 'C:\\Users\\SNEHA MANDAL\\OneDrive\\Desktop\\favsongs'
            songs= os.listdir(music_dir)#lists all song present in directory
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'tell the time' in query:
            strtime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strtime}")
        elif 'open code ' in query:
            codepath ="C:\\Users\\SNEHA MANDAL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'email to sneha' in query:
            try:
                speak("what should i send")
                content= takeCommand()
                to="snehacreative2016@gmail.com"
                sendEmail(to , content)
                speak('email has been sent ')
            except Exception as e:
                print(e)
                speak("Sorry my dear..unable to deliver your email")
        elif 'quit' in query:
               exit()





            
            


    