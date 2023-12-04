# Run this command in terminal  before executing this program
# rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
# and also run this in separate terminal
# rasa run actions

import requests
import speech_recognition as sr  # import the library
# import subprocess
from gtts import gTTS
from playsound import playsound
import os
import pyttsx3

engine = pyttsx3.init()

bot_message = ""
message = ""

r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "Hello"})

print("Bot says, ", end=' ')
for i in r.json():
    bot_message = i['text']
    print(f"{bot_message}")

myobj = engine.say(bot_message)
engine.save_to_file(myobj, 'speech.wav')
engine.runAndWait()
playsound('speech.wav')
os.remove('speech.wav')

while bot_message != "Bye" or bot_message != 'thanks':
    
    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        audio = r.listen(source)  # listen to the source
        try:
            message = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
            print("You said : {}".format(message))
            # To enable translation, uncomment below 2 lines and comment the above line
            # translator = Translator(to_lang='en')
            # print("You said : {}".format(translator.translate(message)))

        except:
            print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly
    if len(message) == 0:
        continue
    print("Sending message now...")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})

    print("Bot says, ", end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")

    myobj = engine.say(bot_message)

    engine.save_to_file(myobj, 'speech.wav')
    engine.runAndWait()

    playsound('speech.wav')
    os.remove('speech.wav')