import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# to execute function directly
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        print('listening..')
        audio = r.listen(source)
    try:
        print('Recognizing..')
        command = r.recognize_google(audio, language='en-in')
        # print(f'command:{command}\n')
        # speak(command)

    except Exception as e:
        pass
        # print('sorry mt say that again please..')
        return 'none'
    return command


if __name__ == '__main__':
    takecommand()



    while True:
        command = takecommand().lower()
        if 'hello sk' in command:
            speak('hello mt')
        elif 'calculate' in command:
            from claculate import wolfram
            from claculate import calc
            command = command.replace('calculate', '')
            calc(command)
            wolfram(command)












# logic are written here to execute task


