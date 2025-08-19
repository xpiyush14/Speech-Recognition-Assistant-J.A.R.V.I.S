#Fist thing will be to import all the neccessaru modules-->
import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import pyjokes
import os
import time

#-->Define a function that will convert our speech into text
def sptext():
    recognizer=sr.Recognizer() #Calling the Recognizer class
    with sr.Microphone() as source:
        print("J.A.R.V.I.S Listening...")#Speak after this is printed..
        recognizer.adjust_for_ambient_noise(source) #Removes noise from background
        #Ek audio func. define kro joh ki source se aaye data ko listen kre
        audio=recognizer.listen(source)
      #THIS try and expect here will read the data and if it is not clear it will throw a pop-up
        try:
            print("RECOGNIZING...") #Bta rhaa h ki haa data record hogya h..
            data=recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Sorry..I didn't Understand..")

#-->Now lets create a function for text to speech for our Jarvis..
def speechtx(x):
    engine = pyttsx3.init() #init here is a class of the pyttsx3 module and we will use its functions..
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id) #Setting the property of the voice 0-Male, 1-Female
    rate = engine.getProperty('rate')
    engine.setProperty('rate',120) #Setting the rate of the voice to 150(Speed->fast,slow)
    engine.say(x)  #Enables our assistant to say anything which is stored in 'x'
    engine.runAndWait()

if __name__ == '__main__': #This special statement will seprate the code written above it from the code written below it.    
    #if sptext().lower() == "hello jarvis":
    while True: #-->SO that our assistant won't stop after only oe instruction..
            data1 = sptext().lower()
            if "your name" in data1:
                name = "my name is jarvis"
                speechtx(name)
                pass
            if "hello" in data1:
                intro = "Hello User"
                speechtx(intro)
                pass
            if"do you do" in data1:
                work = "I am a voice assistant designed to help you"
                speechtx(work)
                pass
        #-->For age of our assistant
            if "old are you" in data1:
                age = "i was born today"
                speechtx(age)
                pass
        #-->For The current time status
            if "time" in data1:
                time1 = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time1)
            # %I-hours, %M-Minutes, %p-A.M. or P.M.
                pass
        #-->Opening Youtube
            if "youtube" in data1:
                webbrowser.open('https://www.youtube.com/')
                pass
        #-->Opening Hianime site
            if "anime" in data1:
                webbrowser.open('https://hianime.to/home')
                pass
        #-->Opening Google
            if "google" in data1:
                webbrowser.open('https://www.google.com/')
                pass
        #-->My LinkedIn
            if "linked" in data1:
                webbrowser.open("www.linkedin.com/in/piyush-mahto-7993b6290")
                pass
        #To get any random pre-installed jokes
            if "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en",category="neutral")
                print(joke_1)
                speechtx(joke_1)
                pass
        #-->Playing any song on the device
            if "song" in data1:
                add='D:\STUDY MATERIAL(REAL)\Songs'
                listsong = os.listdir(add)
                os.startfile(os.path.join(add,listsong[0]))
        #-->Definining an exit point of our assistant
            if "exit" in data1:
                speechtx("Thanks for Using me")
                break
            time.sleep(2)
        #-->At last giving a time delay after execution of each instruction    
    #else:
     #   print("Thanks")
