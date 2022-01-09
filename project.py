import pyttsx3
import datetime
import wikipedia
import random
import webbrowser
import speech_recognition as sr
import os
engine = pyttsx3.init('sapi5')  #voice ko lene ke liye
voices = engine.getProperty('voices')


# print(voices)
engine.setProperty('voices',voices[1].id)
# print(voices[1].id)   


def speak(audio):    
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 | hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good Night")

    speak("I am Jarvis! Sir, How may i help you")
def takeCommand():
    # '''
    #     audio ko le rha hai aur string me convert karke return kar rha hai
    #     Takes mycrophone input from the user
    #     and returns string output
    # '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
         print("Recognising...")
         query = r.recognize_google(audio, language='en-in')
         print(f"user said :{query}\n")   
    except Exception as e:
        # print(e)
        speak("Say that again...")
        # takeCommand()
        # return "none"
    return query
if __name__ == '__main__':
    #  wishMe()
    #  while True:

        query =  takeCommand()
        # query = 'xhamster'
        print(query)
        if 'wikipedia' in query.lower():
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'youtube' in query.lower():
            webbrowser.open("youtube.com")
        elif 'open google' in query.lower():
            webbrowser.open("google.com")
        elif 'facebook' in query.lower():
            webbrowser.open("facebook.com")   
        elif 'music' in query.lower():
            path = "F:\\Python-projects\\music"  
            song = os.listdir(path)
            # r = random.randint(5)
            os.startfile(os.path.join(path, song[random.randint(0, len(song))]))      
        #     songs  = os.listdir("music")
        #     os.startdir(os.path.join(music, songs[0]))
        elif 'time' in query.lower():
            strTime = datetime.datetime.now().strftime("%H : %M : %S")
            speak(f"The time is{ strTime}")
        elif 'code' in query.lower():
            path = "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        # elif 'movies' in query.lower():
        

        #     hollywood_songs = 'F:\Python-projects\pygame_project\hollywood song'
        #     songs = os.listdir(hollywood_songs)
        #     print(songs)
        #     os.startdir(os.path.join(hollywood_songs, songs[0]))
        # # elif 'xhamster' in query.lower():
        #     webbrowser.open("xhamster.com")

        # import os 
# print(dir(os))
# print(os.getcwd())

# os.chdir("C:\\")     #directory change kar dega
# print(os.getcwd())    #directory bataga kaha par hai

# f = open("test.py")

# print(os.listdir("F:\Python"))    #sari files ko print kar dega list me
# a = os.listdir("F:\Python")
# for item in a:
#     print(item) 

# os.mkdir("this/that")   #error ayega kyuki this folder abhi bna nahi hai
# os.makedirs("is/hat/van")    #subdir ban jaega
# os.rename("these", "thise")
        else:
            speak("you must have include wikipedia in your query")

     #Logic for tasks 
    #  speak("Alone is  best")
# wishMe()


