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
# from translate import Translator

# sender = input("What is your name?\n")

bot_message = ""
message = ""
# To enable translation, uncomment the below 2 lines
# translator = Translator(to_lang='hi')
# translation = translator.translate("hello")

r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "Hello"})

print("Bot says, ", end=' ')
for i in r.json():
    bot_message = i['text']
    print(f"{bot_message}")

myobj = gTTS(text=bot_message)
# To enable translation, uncomment below line and comment the above line
# myobj = gTTS(text=translator.translate(bot_message),lang='hi')
myobj.save("speech.mp3")
print('saved')
# Playing the converted file
# subprocess.call(['vlc', "welcome.mp3", '--play-and-exit'])
playsound('speech.mp3')
os.remove('speech.mp3')
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

    myobj = gTTS(text=bot_message)
    # To enable translation, uncomment below 2 lines and comment the above line
    # translator = Translator(to_lang='hi')
    # myobj = gTTS(text=translator.translate(bot_message))
    myobj.save("speech.mp3")
    print('saved')
    # Playing the converted file
    # subprocess.call(['vlc', "welcome.mp3", '--play-and-exit'])
    playsound('speech.mp3')
    os.remove('speech.mp3')
