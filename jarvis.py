import pyttsx3
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():

    hour = int(datetime.datetime.now().hour)   

    if(hour >= 0 and hour < 12):
        speak("Good morning")

    elif hour >=12 and hour < 18:
        speak("Good Aftrnoon !")

    else:
        speak("Good Evening")
    
    speak("Hello there, I am jarvis, How may i assist you ? ")

def takeCommand():
    #It takes microphoneinput form the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recoginzing...")
            query = r.recognize_google(audio, language = 'en-in')
            print(f"user said: {query}\n")

        except Exception as e:
            print("Say that again please...")
            return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('my-Email@gmail.com', 'my-password') #Enter my id and password 
    server.sendmail('myEmail@gmail.com', to, content)
    server.close()

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'exit' in query:
            exit()

        #Logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.in")

        elif 'open google' in query:
            webbrowser.open("google.in")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\kunda\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\kunda\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codePath)
        elif 'send email' in query:
            try:
                speak("what should I say ?")
                content = takeCommand()
                to = "kundanYourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                speak("sorry my friend kundan, I am unable to send email")
                