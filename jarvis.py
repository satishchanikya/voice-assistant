import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
import json
from urllib.request import urlopen 
import time
import wolframalpha

engine=pyttsx3.init()
wolframalpha_app_id = 'wolfram alpha id will go here'
#speak audio from the user input
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# audio for the time in a system
def time_():
    Time=datetime.datetime.now().strftime("%I:%M:%S")# 12 hours(I) and we can use 24 hours (H)
    speak("The current time is :")
    speak(Time)
# speak the date 
def date():
    year=datetime.datetime.now().year 
    month=datetime.datetime.now().month
    day=datetime.datetime.now().day
    speak("the current date is ")
    speak(date)
    speak(year)
    speak(month)
    speak(day)
  #wishing a greatings from the jarvis 
def wishme():
   # speak("welcome to jarvis")
    time_()
    #date() 
hour=datetime.datetime.now().hour
if hour>=5 and hour<=12:
        speak("good morning")
elif hour>=13 and hour<=15:
        speak("good afternoon sir ")
elif hour>=16 and hour<=17:
        speak("good evening")
else :
        speak("good night")   
speak("jarvis is at your service how can i help you") 

wishme()

# used to take a command from the user
def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listeningg.....")
        r.pause_threshold =3
        audio = r.listen(source) 
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-US')
        print(query)

    except Exception as e:
        print(e)
        print("say that again ...")
        return "None"
    return query
TakeCommand()

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('mallachanikya22@gmail.com','Satish$123')
    server.sendmail('mallasatish2001@gmail.com',to,content)
    server.close()

def cpu():
     usage=str(psutil.cpu_percent())
     speak('cpu is at'+usage)
     batery = psutil.sensors_battery()
     speak(batery)
def joke():
     speak(pyjokes.get_joke())

def screenshot():
     img = pyautogui.screenshot()
     img.save('C:/Users/malla/OneDrive/Desktop/screenshot.png')
def restart():
     os.system("shutdown /r /t o")
   
#TakeCommand()
if __name__== "__main__":
     #wishme()

     while True:
          query = TakeCommand().lower()
          if 'time' in query:
               time_()
          elif 'date' in query: 
               date()      
          elif 'wikipedia' in query:
               speak("searching.....")   
               query=query.replace('wikipedia','')
               result=wikipedia.summary(query,sentences=4)
               speak('According to wikipedia')
               print(result)
               speak(result)
          elif 'send email' in query:
               try:
                    speak('what should i say?')
                    content=TakeCommand()
                    speak('Who is receiver?')
                    receiver=("Enter receiver's mail:")
                    to = receiver
                    sendEmail(to,content)
                    speak(content)
                    speak('email will have sent.')
               except Exception as e:
                    print(e)
                    speak("unable to send email.")  

          elif 'search in chrome' in query:
               speak('what should I search ?')
               chromepath ='C:Program Files/Google/Chrome/Application/chrome.exe %s'
               search = TakeCommand().lower()
               wb.get(chromepath).open_new_tab(search+'.com')

          elif 'open youtube' in query:
               speak('what should i search  ?')
               search_Term=TakeCommand().lower()
               speak("here we go to youtube")
               wb.open('https://www.youtube.com/results?search_query='+search_Term) 
          elif 'search google' in query:
               speak('what should I search?')
               search_Term= TakeCommand().lower()
               speak("searching....")
               wb.open('https://www.google.com/search?q='+search_Term)
          elif 'cpu' in query:
               cpu()

          elif 'joke' in query:
               joke()    

          elif 'word' in query:
               speak("opening ms-word....")
               ms_word = r'C:Program Files/Microsoft Office/root/Office16/WINWORD.EXE'
               os.startfile(ms_word)
          elif 'file manager' in query:
               speak("opening your file manager....!")
               open_file=r'C:/Users/malla/OneDrive/Desktop'
               os.startfile(open_file)
          

          elif 'write a note' in query:
               speak("what should I write, sir?")
               notes = TakeCommand()  
               file = open('notes.txt','w')
               speak("should i include date and time")
               ans = TakeCommand()
               if 'definitely' in ans:
                    strTime=datetime.datetime.now().strftime('%H:%M:%S')
                    file.write('strTime')
                    file.write(':-')
                    file.write(notes)
                    speak('done taking notes sir')
               else:
                    file.write(notes) 

          elif 'showing note' in query:    
               speak('showing notes')
               file=open('notes.txt','r')
               print(file.read())
               print(file.read())
                
          elif 'screenshot' in query:
               screenshot() 
          elif 'good morning' in query:
               speak('how can i help you') 
          elif 'good morning' in query:
               speak('how can i help you') 
          elif 'good morning' in query:
               speak('how can i help you')     
          elif 'how are you' in query:
               speak("I am fine thank you.what about you") 
          elif 'tell me about yourself' in query:
               speak('''I am a latest networking services. Including in the AI and ML.
                     I am an advanced virtual assistant capable of understanding and generating human-like text based on the input I receive.
                     If you want to any questions feel free to ask.''') 
          elif 'play music' in query:
               song_dir =('C:/Users/malla/Music')
               music =os.listdir(song_dir)
               speak("which I want to play")
               ans = TakeCommand().lower()
               no=int(ans.replace('number',''))
               os.startfile(os.path.join(song_dir,music[no]))   

          elif 'news' in query:
            try:
             #  jsonobj = urlopen("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=218ce945afd742a4aa8153f85f731dcb")
               jsonobj1 = urlopen("https://newsapi.org/v2/top-headlines?country=us&apiKey=218ce945afd742a4aa8153f85f731dcb")
               data =json.load(jsonobj1)
               i = 1
               speak("here are some top headlines about your search")
               print("========= TOP HEADLINES =========="+'\n')
               for item in data['articles']:
                    print(str(i)+'.'+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1
            
            except Exception as e:
                 print(str(e))

          elif 'remember that' in query:
               speak('what should i remember?')
               memory = TakeCommand()
               speak('you asked me to remember that'+memory)
               remember = open('memory.txt','w')       
               remember.write(memory)
               remember.close()

          elif 'do you remember anything' in query:
               remember = open('memory.txt','r')
               speak('you asked me to remember that'+remember.read())   

          elif 'where is' in query:
               query= query.replace("where is","")
               location = query
               speak('user asked to locate'+location)
               wb.open_new_tab("https://www.google.com/maps/place/"+location)   
          elif 'calculate' in query:
               client = wolframalpha.Client(wolframalpha_app_id)
               index = query.lower().split().index('calculate')
               query = query.split()[index + 1:]
               #res=client.query(''.join(query))    
               res1 = client.query(''.join(query))     
               answer = next(res1.results).text
               print('The Answer is : '+answer)
               speak('The Answer is '+answer)
          elif 'stop listening' in query:
               speak('for how many minutes you want me to stop listening')
               ans =int(TakeCommand())
               time.sleep(ans)
               print(ans)
          elif 'exit' in query:
               speak("jarvis going to ofline!")
               quit()