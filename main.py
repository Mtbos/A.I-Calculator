import speech_recognition
import pyttsx3
import wolframalpha


# This file is for Calculate area used in main file 



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wolfram(query):
    apikey = 'WWXL9P-AXV3Q2J9K3'
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak('sorry mt could not find the value')

def calc(query):
    term = str(query)
    term = term.replace('sk', '')
    term = term.replace('multiply', '*')
    term = term.replace('plus', '+')
    term = term.replace('minus', '-')
    term = term.replace('divide', '/')
    term = term.replace('square root of', '')
    Final = str(term)
    try:
        result = wolfram(Final)
        speak(result)
        print(result)
    except:
        speak('sorry mt i can find the such type of value')
