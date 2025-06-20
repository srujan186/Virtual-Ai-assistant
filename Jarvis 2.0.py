import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition  
import pyaudio #pip install pyaudio
import smtplib 
from email_secrets import senderemail, epwd, to 
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import requests
import os
import clipboard as cp
import pyjokes
import time as tt
import string
import random
import psutil
from nltk.tokenize import word_tokenize


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

wakeword = 'jarvis'

def getvoices(voice):
    global wakeword 
    voices = engine.getProperty('voices')
    if voice == 1:
        engine.setProperty('voice', voices[1].id)
        wakeword = 'jarvis'
        speak("hello this is jarvis")
    elif voice == 2:
        engine.setProperty('voice', voices[2].id)
        wakeword = 'friday'
        speak("hello this is friday")
        
def time():
        Time = datetime.datetime.now().strftime("%I:%M:%S")
        speak("the current time is")
        speak(Time)

def date():
        year = str(datetime.datetime.now().year)
        month = str(datetime.datetime.now().month)
        date = str(datetime.datetime.now().day)
        speak("the current date is")
        speak(date)
        speak(month)
        speak(year)

# while True:
#     try:
#         voice = int(input("enter the voice number 1 for jarvis :\nAnd 2 for Friday:\n"))
#         if voice in [1, 2]:
#             getvoices(voice)
#         else:
#             print("Please enter a valid number (1 or 2).")
#     except ValueError:
#         print("Invalid input. Please enter a number.")
def wishme():
    speak("welcome back sir!")

    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")
    elif hour >= 18 and hour < 24:
        speak("Good evening sir!")
    else:
        speak("Good night sir!")
    speak("Jarvis at your service. Please tell me how can I help you today?")
# wishme()

def takecommandCMD():
    query = input("Please tell me how can I help you today\n")
    return query

def takecommandMIC():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

def sendemail(receiver,subject,content1):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content1)
    server.send_message(email)
    server.close()

def whatsappmsg(phone_number, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_number+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')

def searchgoogle():
    speak("What should I search for?")
    search = takecommandMIC()
    url = 'https://www.google.com/search?q=' + search
    wb.open(url)
    speak("Here is what I found for " + search)

def playonyt(search):
    url = f"https://www.youtube.com/results?search_query={search}"
    wb.open(url)
    print(f"Playing {search} on YouTube")

def get_weather(city):
    
    complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=6d326048b372c949ef8a2e93c2236367&units=metric"
     
    try:
        response = requests.get(complete_url)
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        weather = data['weather']
        weather_description = weather[0]['description']
        speak(f"Temperature: {temperature}°C")
        speak(f"Humidity: {humidity}%")
        speak(f"Pressure: {pressure}hPa")
        speak(f"Weather: {weather_description}")

    except Exception as e:
        print(e)
        speak("Sorry sir! I am not able to fetch the weather details at the moment.")

def open_application(app_name):
    try:
        # Define paths for commonly used applications
        app_paths = {
            "notepad": "C:\\Windows\\System32\\notepad.exe",
            "calculator": "C:\\Windows\\System32\\calc.exe",
            "chrome": "C:\\Users\\sushma s\\Downloads\\ChromeSetup.exe",
            "tableau": "C:\\Users\sushma s\\Downloads\\TableauPublicDesktop-64bit-2024-3-0.exe"
        }

        if app_name in app_paths:
            os.startfile(app_paths[app_name])
            speak(f"Opening {app_name}")
        else:
            speak("Sorry, I don't know the path to that application.")
    except Exception as e:
        print(e)
        speak("Unable to open the application.")

def text2speech():
    text = cp.paste()
    print(text)
    speak(text)

def screenshot():
    name_img = tt.time()
    name_img = f"C:\\Users\\sushma s\\Desktop\\Srujan\\jarvis 2.0\\screenshot\\{name_img}.png"
    img = pyautogui.screenshot()
    img.show()       
        
def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlen = 8
    s = []
    s.extend(list(s1)) 
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))  

    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print(newpass)

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage + "%")
    battery = psutil.sensors_battery()
    speak(" battery percentage is at " + str(battery.percent) + "%")
    if battery.power_plugged:
        speak("plugged in")
    else:
        speak("not plugged in")

def greetings():
    global wakeword
    getvoices(0)
    speak(wishme())

    while True:
        query = takecommandMIC().lower()
        query = word_tokenize(query)
        print(query)
        if wakeword in query:
            if 'time' in query:
                time()
            elif 'date' in query:
                date()
            elif 'tell me' in query:
                speak(" Kavya was born on 15th May 2004 in Banglore, kavya loves to draw and organizing the event")
            elif 'switch' in query:
                getvoices(2)
            elif 'email' in query:
                email_list = {

                    'email one' : 'srujansrinivas5045@gmail.com',
                    'Kavya' : 'kavyarudra15@gmail.com' 
                }
                try:
                    speak("To whom should I send the email?")
                    name = takecommandMIC()
                    if name in email_list:
                        receiver = email_list[name]
                        speak("What is the subject of the email?")
                        subject = takecommandMIC()
                        speak("what should i say?")
                        content1 = takecommandMIC()
                        sendemail(receiver,subject,content1)
                        speak("Email has been sent!")
                    else:
                        speak("Sorry sir! I am not able to send this email")
                except Exception as e:
                    print(e)
                    speak("Unable to send the email")

            elif 'whatsapp' in query:
                user_name = {
                    'Kavya' : '+91 97319 97835',
                    'Sushma' : '+91 82175 65398'
                }
                try:
                    speak("To whom should I send the whatsapp message?")
                    name = takecommandMIC()

                    if name in user_name:
                        phone_number = user_name[name]
                        speak("What is the message?")
                        message = takecommandMIC()
                        whatsappmsg(phone_number,message)
                        speak("Whatsapp message has been sent!")
                        
                    else:
                        speak("Sorry sir! I am not able to send this message")
                except Exception as e:
                    print(e)
                    speak("Unable to send the whatsapp message")

            elif 'search' in query:
                searchgoogle()

            elif 'youtube' in query:
                speak("what should i search in Youtube?")
                search = takecommandMIC()
                playonyt(search)

            elif 'weather' in query:
                speak("which city weather you want to know?")
                city = takecommandMIC()
                get_weather(city)
                speak("Here is the weather report for " + city)
                
            elif 'open' in query:
                speak("Which application should I open?")
                app_name = takecommandMIC().lower()
                open_application(app_name)
        
            elif 'document' in query:
                speak("opening the document")
                os.system('explorer C://{}'.format(query.replace('open', '')))

            elif 'read' in query:
                speak(text2speech())

            elif 'joke' in query:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)
            
            elif 'screenshot' in query:
                screenshot()
                speak("Screenshot has been taken!")    

            elif 'remember' in query:
                speak("what should I remember?")
                data = takecommandMIC()
                speak("storing" + data + "in memory")
                remember = open('data.txt', 'w')
                remember.write(data)
                remember.close()

            elif 'recall' in query:
                remember = open('data.txt', 'r')
                speak("you asked me to remember that" + remember.read())

            elif ' password' in query:
                speak("generating the password")
                passwordgen()
                speak("password has been generated")

            elif 'performance' in query:
                cpu()

            elif 'goodbye' in query:
                speak("Good bye sir! Have a nice day!")
                quit()
            
            else:
                speak("I am sorry sir! I am not programmed to do that task.")
greetings()

