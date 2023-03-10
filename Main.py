import speech_recognition as sr
import pyttsx3
import pywhatkit #it plays youtube after giving command
import datetime
import wikipedia



#creating a listener which recognize the comand
listener = sr.Recognizer()
#text to speech converter
engine = pyttsx3.init()

voices=engine.getProperty('voices')
#here we are passing voices[1] that means audio will play in female voice
#and voices[0] is for male voice .maximum 0 and 1 are allowed not more than that
engine.setProperty('voice', voices[1].id)

#whatever will be the input command this function will convert t into text and wait
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command(): #3rd me yha aayega execution
    try:
        #it use microphone to listen our voice
        with sr.Microphone() as source:
            print('listening.....')
            #creating a variable voice which listen and store the voice
            voice = listener.listen(source)
            #by using google api here voice is converted into text
            command = listener.recognize_google(voice)
            #it will convert given command to upper case letters while showing
            x = command.lower()
            if 'Alexa' in command:
                command = command.replace('Alexa', '') #or 4th me jb yha se alexa command mil jayega
                ## to run alexa() fun me return ho jayega
                #playonyt means playing something in youtube

    except:
           pass
    return command

def run_alexa():
    command = take_command()  # 2nd after getting take_command()it will pass on this fun
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        print(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('current time is ' + time)
    elif 'who' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'what' in command:
        person = command.replace('what', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'where' in command:
        person = command.replace('where', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'which' in command:
        person = command.replace('which', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'how' in command:
        person = command.replace('how', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'when' in command:
        person = command.replace('when', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

while(True):
    run_alexa() #1st compiler will come on this
