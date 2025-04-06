import pyttsx3    #pip install pyttsx3
import datetime
import speech_recognition as sr    #pip install speechRecognition
import wikipedia  #pip install wikipedia
import smtplib
import webbrowser as wb
import psutil #pip install psutil           for battery and currnt cpu situatiion
import pyjokes #pip install pyjokes
import os
import pyautogui #pip install pyautogui (For Screenshot)
import random
import operator
import wolframalpha #pip install wolframalpha
import json
import requests
from urllib.request import urlopen
import time
import pyglet
import winshell             #pip install winshell
import pyglet
import tkinter
import cv2
import ctypes
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import calendar
from tkinter import *



def main():

    engine=pyttsx3.init()
    wolframalpha_app_id = 'EAYTJT-2R9XP5AKKA'

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def _time_():
        time=datetime.datetime.now().strftime("%I hours %M minutes and %S seconds") #for 12 hour clock    %H for 24 hour clock    
        speak("The current time is"+time)   

    def _date_():
        '''year=datetime.datetime.now().year
        month=datetime.datetime.now().month
        date=datetime.datetime.now().day
        speak("The current date is")
        speak(date)
        speak(month)
        speak(year)'''
        now=datetime.datetime.now()
        date=datetime.datetime.today()
        weekday=calendar.day_name[date.weekday()]
        month=now.month
        year=datetime.datetime.now().year
        daynum=now.day

        month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                    'November', 'December']

        ordinalnumbers = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14th','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']

        speak('Today is ' + weekday + 'and todays date is '+ordinalnumbers[daynum-1]+','+month_names[month-1])
        speak(year)

    def day():
        
        # This function is for telling the day of the week
        day = datetime.datetime.today().weekday() + 1
        
        #this line tells us about the number that will help us in telling the day
        day_dict = {1: 'Monday', 2: 'Tuesday', 
                    3: 'Wednesday', 4: 'Thursday', 
                    5: 'Friday', 6: 'Saturday',
                    7: 'Sunday'}
        
        if day in day_dict.keys():
            day_of_the_week = day_dict[day]
            print(day_of_the_week)
            speak("The day is " + day_of_the_week)

    def welcomeme():
        speak("Welcome back SIR")
        _time_()
        _date_()

        hour=datetime.datetime.now().hour

        if hour>=6 and hour<12:
            speak("Good Morning Sir!")
        
        elif hour>=12 and hour<17:
            speak("Good Afternoon Sir!")    

        elif hour>=17 and hour<24:
            speak("Good Evening Sir!")    
        
        speak("ZEN the Personal Assistant at your service.How can I help you today??")


    def takecommand():
        r = sr.Recognizer()  # used for recognization to command which we gonna ask

        with sr.Microphone() as source:
            print("Listening......")
            r.path_threshold = 1          # how long it will wait for the user to use
            audio = r.listen(source)

        try:
            print("Recognizing..... ")
            query = r.recognize_google(audio, language='en-US')  # en-us used for the english language to recognize   ,  it wil recognize only command which google is able to recognize
            print(query)

        except Exception as e:
            print(e)
            print("Say that again please.......")
            return "None"
        return query

    def email(to,content):
        server=smtplib.SMTP('smtp.gmail.com',587)       #587 is port for gmail,SMTP is mailing service
        server.ehlo()                                   #help in defining to ESMTP server
        server.starttls()                               #help in putting connection to SMTP server into tls module

        server.login('mahib6504@gmail.com','mahib6504@1999')                             #email address and password of sender
        server.sendmail('mahib6504@gmail.com',to,content)                  #sender email
        server.close()                                  #quit function

    def screenshot():
        img = pyautogui.screenshot()
        img.save("C:/Users/rutvi/OneDrive/Desktop/Python Mini Project/screenshot.png")

    def cpu():
        usage = str(psutil.cpu_percent())
        print("CPU is at"+ usage)
        speak('CPU is at'+ usage)

    def _battery():
        battery = psutil.sensors_battery()
        speak("Battery is at")
        speak(battery.percent)

    def jokes():    
        speak(pyjokes.get_joke())

    def introduction():
        speak("I am Z.E.N 1.0 , Personal AI assistant , "
        "I am created by my master Rutvij , "
        "I can help you in various regards , "
        "I can search for you on the Internet , "
        "I can also grab definitions for you from wikipedia , "
        "In layman terms , I can try to make your life a bed of roses , "
        "Where you just have to command me , and I will do it for you , ")

    def features():
        speak("I can tell yo date,time and current day,"
            "I can search wikipedia and google for you,"
            "I also can search urls for you in different browsers installed on your computer,"
            "I can check your cpu and battery status too,"
            "I can even open applications from your PC for your work to get easy,"
            "I can even write a note for you and also diaplay that for you,"
            "I also know how to send emails so also can do it on behalf of you,"
            "I can even tell you some current news and can also tell you the weather forecast,"
            "I can also locate places for you,"
            "I can also remember things for you as I've very sharp memory and do not forget like humans,"
            "I'm also able to solve some mathematical problems,"
            "I can even play some songs for you,"
            "I can also do some PC stuffs like screnshot the screen empty the recycle bin locking the window log off PC restart PC and also shut down your PC,"
            "If you are photogenic or love to make videos i can even do that for you,"
            "If you have a singing voice i can even record audio for you,"
            "And if you have a plenty of leisure time I can even tell you some jokes and chat with you,"
            "You just order me and assume it as done"
        )

    def purpose():
        speak("I'm created for Python's Mini project purpose," 
            "If you are facing any problem regarding the 'Z.E.N',my makers will definitely help you")


    def camera():
        speak("Opening Camera")
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("ZEN Camera")
        img_counter = 0

        while True:
            ret, frame = cam.read()
            if not ret:
                speak("Failed to open frame")
                break
            cv2.imshow("ZEN Camera", frame)

            k = cv2.waitKey(1)
            
            if k%256 == 27:
                # ESC pressed
                speak("Closing camera...Thank You")
                print("Closing camera...Thank You")
                break
            
            elif k%256 == 32:
                # SPACE pressed
                img_name = "Capture({}).png".format(img_counter)
                cv2.imwrite(img_name, frame)            
                print("{} written!".format(img_name))
                speak("Image captured")
                img_counter += 1

        cam.release()
        cv2.destroyAllWindows()

    def video():     
        speak("Starting Video Camera")    
        speak("Please smile, capturing video")
        #Capture video from webcam
        vid_capture = cv2.VideoCapture(0)
        vid_cod = cv2.VideoWriter_fourcc(*'XVID')
        output = cv2.VideoWriter(r"C:\Users\rutvi\OneDrive\Desktop\Python Mini Project\capture.mp4", vid_cod, 20.0, (640,480))

        speak("Starting in 5")
        time.sleep(0.01)
        speak("4")
        time.sleep(0.01)
        speak("3")
        time.sleep(0.01)
        speak("2")
        time.sleep(0.01)
        speak("1")
        time.sleep(0.01)

        while(True):
            # Capture each frame of webcam video
            ret,frame = vid_capture.read()
            cv2.imshow("ZEN Video Camera", frame)        
            output.write(frame)
            # Close and break the loop after pressing "x" key
            if cv2.waitKey(1) &0XFF == ord('x'):
                break

        # close the already opened camera
        vid_capture.release()
        # close the already opened file
        output.release()
        # close the window and de-allocate any associated memory usage
        cv2.destroyAllWindows()

    def voice():
        # Sampling frequency
        freq = 44100

        # Recording duration
        duration = 10

        # Start recorder with the given values of duration and sample frequency
        speak("Recording started...")
        recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)
        print("Recording....")

        # Record audio for the given number of seconds
        sd.wait(7)

        # This will convert the NumPy array to an audio
        # file with the given sampling frequency
        # write("recording0.wav", freq, recording)

        # Convert the NumPy array to audio file
        wv.write("recording1.wav", recording, freq, sampwidth=2)

        speak("Recording has been Saved Successfully")
        print("Recording Saved Successfully")


    if __name__ == "__main__":
        clear = lambda: os.system('cls')
        welcomeme()       

        while True:                                 # created an infinity loop                  
            query=takecommand().lower()             # All command will be stored is lower case in query for easy Recognization

            if 'time' in query:  # tell us time when asked
                _time_()

            elif 'date' in query:  # tell us date when asked
                _date_()
            
            elif 'which day' in query or 'todays day' in query or 'day' in query:   # tell us day
                day()

            elif 'hello' in query:
                speak("Hello Sir,how can I help you?")

            elif 'introduction' in query or 'introduce' in query:
                introduction()

            elif 'made' in query or 'purpose' in query:
                purpose()

            elif 'what can you do for me?' in query:
                features()
                
            elif 'Good Morning' in query:
                speak("Good Morning Sir,"
                    "whats your agenda for today")

            elif 'Good Afternoon' in query:
                speak("Good Afternoon Sir,"
                    "whats your agenda for today")

            elif 'Good Evening' in query:
                speak("Good Evening Sir,"
                    "whats your agenda for today")

            elif 'Good Night' in query:
                speak("Good Night Sir")
                quit()
            
            elif 'how are you' in query:
                speak("I am fine, Sir Thanks for asking")
                speak("How are you Sir?")
                if 'fine' in query or "good" in query: 
                    speak("It's good to know that your fine")
                else:
                    speak("I hope you get well soon.")

            elif "who am i" in query:
                speak("If you can talk, then definitely you are a human or AI assiatant like me")

            elif "why you came to this world" in query:
                speak("Thanks to my creator. further it is a secret")

            elif 'empty recycle bin' in query:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                speak("Recycle Bin Recycled") 

            elif 'wikipedia' in query:
                speak("Searching.......")
                query=query.replace('wikipedia', '')  # replace wikipedia with blank
                result=wikipedia.summary(query, sentences=4)
                speak('According to Wikipedia')
                print(result)
                speak(result)

            elif 'send email' in query:
                try:
                    speak("What should I say")
                    content=takecommand()

                    #Provide Receivers Email Address
                
                    speak("Who is the receiver??")
                    receiver=input("Enter receivers email address:")
                    to=receiver
                    email(to,content)               
                    speak('Email has been sent')

                except Exception as e:
                    print(e)
                    speak("Unable to send")

            elif 'search in firefox' in query:
                
                speak("What should I search??")
                path='C:/Program Files/Mozilla Firefox/firefox.exe %s'                               #path is loacation of browser(firefox) installation on computer
                search = takecommand().lower()                                                    
                wb.get(path).open_new_tab(search+'.com')                                          #pre-build function of webbrower library to open search in new tab
                                                                                                #this function only work for website ending with ".com"

            elif 'search in edge' in query:
                
                speak("What should I search??")
                path='C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s'
                search = takecommand().lower()                                                    
                wb.get(path).open_new_tab(search+'.com') 

            elif 'open youtube' in query:

                speak("What should I search?")
                Search_term = takecommand().lower()     
                speak("Here we go to Youtube\n")
                wb.open("https://www.youtube.com/results?search_query="+Search_term)
                _time_.sleep(5)

            elif 'search google' in query:
                print("What should I search for you??")
                speak("What should I search for you??")
                Search_term = takecommand().lower()
                wb.open('https://www.google.com/search?q='+Search_term) 

            elif 'cpu' in query:
                cpu()   
            
            elif 'battery' in query:
                _battery()

            elif 'joke' in query:
                jokes()

            elif 'word' in query:
                speak("opening MS Word")
                word = r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'
                os.startfile(word)

            elif 'open codeblocks' in query:
                speak("Opening Codeblocks Compiler")
                codeblocks=r'D:\Program Files\CodeBlocks\codeblocks.exe'
                os.startfile(codeblocks)

            elif 'open eclipse' in query:
                speak("Opening eclipse")
                eclipse=r'D:\eclipse\eclipse.exe'
                os.startfile(eclipse)

            elif "write a note" in query:
                speak("What should i write, sir")
                note = takecommand()
                file = open('note.txt', 'w')            #opens file in write mode 
                speak("Sir, Should i include date and time")
                dt = takecommand()
                if 'yes' in dt or 'sure' in dt:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                    speak('done')
                else:
                    file.write(note)
                    speak('done')

            elif "show note" in query:
                speak("Showing Notes")
                file = open("note.txt", "r")        #opens file in read mode
                print(file.read())
                speak(file.read())

            elif 'screenshot' in query:
                screenshot()
                speak("Done!")   

            elif 'play songs' in query:
                audio = r'C:\Users\rutvi\Music\Audio'                    
                songs_dir = audio
                songs = os.listdir(songs_dir)
                print(songs)

                speak("select any number")
                rand = int(takecommand())
                random = os.startfile(os.path.join(songs_dir, songs[rand]))                                          
                time.sleep(7)

            elif 'play videos' in query:
                video =r'E:\Maxtor\Rutvij\Videos'
                video_dir = video
                videos = os.listdir(video_dir)
                print(videos)

                speak("select a random number")
                ran = int(takecommand())
                random_1 = os.startfile(os.path.join(video_dir, videos[ran]))
                time.sleep(7)

            elif 'open photos' in query:
                speak("opening Photos")
                photo = r'E:\Maxtor\Rutvij\Images'
                photo_dir=photo
                photos=os.listdir(photo_dir)
                print(photos)

                speak("select a random number")
                rand1 = int(takecommand())
                random_ = os.startfile(os.path.join(photo_dir,photos[rand1]))
                time.sleep(7)

            elif "weather" in query:
                
                # paste your api key here
                api_key = "Your api key"

                # getting city name from user
                speak("City Name:")            
                city = takecommand()

                """
                we appending the city valirable and api_key variable to complete the url. for example city name is Mumbai  then url looks like 
                https://api.openweathermap.org/data/2.5/weather?q=Mumbai&units=metric&APPID=cb44790e87950f163636975c2aba3f6e
                
                """
                data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")

                # uncomment the following line and run it so you can get the data in json format
                #print(data.json())
                
                # getting the data
                print(f"Location: {data.json().get('name')}, {data.json().get('sys').get('country')}")
                speak(f"Location: {data.json().get('name')}, {data.json().get('sys').get('country')}")
                
                print(f"Temperature: {data.json().get('main')['temp']}°C")
                speak(f"Temperature: {data.json().get('main')['temp']}°C")
                
                print(f"Weather: {data.json().get('weather')[0].get('main')}")
                speak(f"Weather: {data.json().get('weather')[0].get('main')}")
                
                print(f"Min/Max Temperature: {data.json().get('main')['temp_min']}°C/{data.json().get('main')['temp_max']}°C")
                speak(f"Min/Max Temperature: {data.json().get('main')['temp_min']}°C/{data.json().get('main')['temp_max']}°C")
            
                print(f"Humidity: {data.json().get('main')['humidity']}%")
                speak(f"Humidity: {data.json().get('main')['humidity']}%")
                
                print(f"Wind: {data.json().get('wind')['speed']} km/h")
                speak(f"Wind: {data.json().get('wind')['speed']} km/h")

        
            elif 'remember that' in query:                                              #set reminder
                speak("What should I remember?")
                memory = takecommand()
                speak("You asked me to remember that"+memory)
                remember = open('memory.txt','w')
                remember.write(memory)
                remember.close()

            elif 'do you remember anything' in query:
                remember = open('memory.txt','r')
                speak('You asked me to remember that'+remember.read())

            elif 'where is' in query:
                query = query.replace("where is","")
                location = query
                speak("User asked to locate"+location)
                wb.open_new_tab("https://www.google.com/maps/place/"+location)

            elif 'news' in query:
                try:
                    jsonObj = urlopen("https://newsapi.org/v2/top-headlines?country=in&apiKey=yourapikey")
                    data = json.load(jsonObj)
                    i=1

                    speak('Here are some top headlines')
                    print('========TOP HEADLINES======='+'\n')
                    for item in data['articles']:
                        print(str(i)+'.'+item['title']+'\n')
                        print(item['description']+'\n')
                        speak(item['title'])
                        i += 1

                except Exception as e:
                        print(str(e))


            elif 'calculate' in query:
                client = wolframalpha.Client(wolframalpha_app_id)
                index1 = query.lower().split().index('calculate')
                query = query.split()[index1 + 1:]
                res  = client.query(''.join(query))
                answer = next(res.results).text
                print('The Answer is : '+answer)
                speak('The Answer is : '+answer)


            elif 'what is' in query or 'who is' in query:
                #use the same API key that we earlier i.e. wolframalpha
                client = wolframalpha.Client('yourapikey')
                res = client.query(query)

                try:
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except StopIteration:
                    print('No results')      
                

            elif "camera" in query or "take photo" in query:            
                camera()

            elif "video" in query or "record video" in query:            
                video()          

            elif 'voice' in query or "record audio" in query:
                voice()

            elif 'stop listening' in query or 'dont listen' in query:
                speak('For how many second you want me to stop listening to your commands?')
                ans = int(takecommand())
                time.sleep(ans)
                print(ans)

            elif 'lock window' in query:
                    speak("locking the device")
                    ctypes.windll.user32.LockWorkStation()

            elif 'log out' in query or 'sign out' in query or 'log off' in query:
                os.system('shutdown -l')

            elif 'restart' in query:
                speak("Hold On a Sec ! Your system is on its way to restart")
                os.system("shutdown -t 0 -r -f")

            elif 'shutdown' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                os.system("shutdown /s /t 1")

            elif 'offline' in query or 'bye' in query:
                speak("going Offline")
                time.sleep(0.1)
                speak("Thank you sir")
                quit()                                                           #quit

main()
               
            


