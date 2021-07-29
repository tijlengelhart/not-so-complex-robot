import datetime
import webbrowser
import subprocess
import pyjokes
import pyttsx3
import speech_recognition as sr

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
error = False
Searching= False



def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print ('staring up command')
            print('listening...')
            talk ('i am listening') and print ('starting up completed')
            voice = listener.listen(source)
            print ('testing command')
            command = listener.recognize_google(voice)
            print ('2nd test on command')
            command = command.lower()
            print ('3th test on command')
            if 'alexa' in command:
                print ('command fully anylised and has been completed')
                command = command.replace('alexa', '')
                print(command)


    except:
        print ("error")



    return command


def run_alexa() -> object:
    command = take_command()
    print(command)

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print ('time command completed')
    elif 'date' in command:
        talk('sorry, I have a headache')
        print ('date command completed')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
        print('single command completed')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print ('joke command completed')
    elif 'hello' in command:
        talk ('hi')
        print ('hello command completed')
    elif 'thank you' in command:
        talk ('no problem')
        print ('thanks command completed')
    elif 'search' in command:
        _searchrequest = command.replace('search', '')
        webbrowser.open_new("https://www.bing.com/search?q=" + _searchrequest)
        print ('search command completed')
        print ('user has searched for ' + _searchrequest)
    elif 'what is the time' in command:
        _time = datetime.time
        print (_time)
        talk (_time)
    elif 'open' in command:
        _fileopen = command.replace('open ', '').lower()
        if 'minecraft' in _fileopen:
            print('opening Minecraft')
            subprocess.Popen('C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe')
        elif 'notepad' in _fileopen:
            print('opening Notepad')
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
        else:
            print('no')

##project finished... it was finished on 7/29/2021 11:25AM








    else:
        talk ('i couldnt understand that')




while True:
    print ('NOTE: '
           'if this is a started up message nothing is wrong'
           'this message is also a reloader of the function command '
           'if this is not a startup then the program '
            'has an ERRORCODE')
    run_alexa()
