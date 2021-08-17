import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import googlesearch
import PyDictionary

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():


        speak("I am Tobi, How can i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio_data=audio, language='en-in')
        print(f"User said: {query}\n")
        print()
    except Exception as e:
        print("pardon me. please say that again...")
        speak("pardon me sir. please say that again")
        return "None"
    return query


def takeCommand1():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio_data = r.listen(source)

    try:
        print("Recognizing...")
        query1 = r.recognize_google(audio_data, language='en-in')
        print(f" {query1}\n")
        print()
    except Exception as e1:
        print("pardon me. please say that again...")
        speak("pardon me sir. please say that again")
        return "None"
    return query1


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("d.codeblooded@gmail.com", "qwerty67890")
    server.sendmail("d.codeblooded@gmail.com", to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.com")

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")

        elif 'open hackerrank' in query:
            webbrowser.open("hackerrank.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open college website' in query:
            webbrowser.open("https://www.sirmvit.edu/")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The Time is {strTime}")
            print(strTime)
        elif 'shutdown' in query:
            break
        elif 'send an email' in query: 
           
            try: 

                speak("Whom do you want to send an email,sir")
                
                to = takeCommand()
                if 'myself' in query: 
                    myself = "asauravraj16@gmail.com"
                    to = myself
                    print("sending email to " + to)
                elif 'dad' in query:
                    dad = "ashutoshofc123@gmail.com"
                    to = dad
                    print("sending email to " + to)
                elif 'ritesh' in query:
                    ritesh = "rk301999@gmail.com"
                    to = ritesh
                    print("sending email to " + to)
                elif 'abhishek' in query:
                    abhishek = "abhiabhikr7@gmail.com"
                    to = abhishek
                    print("sending email to " + to)
                elif 'supriya' in query:
                    supriya = "supriya_cs@sirmvit.edu"
                    to = supriya
                    print("sending email to " + to)
                elif 'harshita' in query:
                    harshita = "harshitasaxsena101@gmail.com"
                    to = harshita
                    print("sending email to " + to)
                elif 'suru' in query:
                    suru = "suruchi.mothe@gmail.com"
                    to = suru
                    print("sending email to " + to)
                elif 'arya' in query:
                    arya = "aryapatil1313@gmail.com"
                    to = arya
                    print("sending email to " + to)   
                
                speak("What should i send sir?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent")
                print("Email has been sent")

            except Exception as e:
                    print(e)
                    speak("Sorry sir, i was unable to send the mail")
                    print("email wasnt sent")
        elif'search google' in query:
           from googlesearch.googlesearch import GoogleSearch
response = GoogleSearch().search("something")
for result in response.results:
    print("Title: " + result.title)
    print("Content: " + result.getText())
        
         
            
