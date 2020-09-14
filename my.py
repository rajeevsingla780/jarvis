import pyttsx3
import datetime
import speech_recognition as sr
import sys
import wikipedia
import webbrowser
import os
import smtplib
import random
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour < 12):
        speak("Good Morning")
    elif (hour > 12 and hour < 18):
        speak("Good Afternoon")
    else:
        speak("Good night")
    speak("I am Jarvis Sir ,How may i help you")


def Take_Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language="en-in")
        print("User said ", query,"\n")
    except Exception as e:
        print("Say That again please")
        return "None"
    return query
def sendEmail(to,con):
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo
	server.starttls()
	server.login("rajeevsingla780@gmail.com","rsingla08102001")
	server.sendmail("rajeevsingla780@gmail.com",to,con)
	server.close()


if __name__ == '__main__':
    wishMe()
    while(True):
        query=Take_Command().lower()
        if 'wikipedia' in query:
        	speak('Searching Wikipedia....')
        	query=query.replace("wikipedia","")
        	results=wikipedia.summary(query,sentences=2)
        	speak("According to wikipedia")
        	speak(results)
        elif 'goodbye' in query:
        	speak("Good bye Sir have a good day ahead")
        	quit()	
        elif 'open youtube' in query:
        	webbrowser.open("youtube.com")
        elif 'open google' in query:
        	webbrowser.open("google.com")	
        elif 'play music' in query	:
        	mydir="F:\\music"
        	songs=os.listdir(mydir)
        	x=random.randint(0,len(songs)-1)
        	os.startfile(os.path.join(mydir,songs[x]))
        elif 'time'	in query:
        	strtime=datetime.datetime.now().strftime("%H:%M:%S")
        	speak("Sir The time is")
        	speak(strtime)
        elif 'open code' in query:
            path="C:\\Users\\RAJEEV SINGLA\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"	
            os.startfile(path)
        elif 'email to rajiv' in query:
            try:
               	speak("What do I say")
               	con=Take_Command()
               	to="rajeevsingla781@gmail.com"
               	sendEmail(to,con)
               	speak("Email has been sent")
            except Exception as e:
            	print(e)
            	speak("Sorry I am not able to send this email")

	     	



