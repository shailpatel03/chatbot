# Chatbot

## Libraries needed to run this chatbot:

* rasa 2.2.9 (run ```pip install rasa==2.2.9``` in command prompt)
* rasa-x 0.38.1 (run ```pip3 install --use-deprecated=legacy-resolver rasa-x --extra-index-url https://pypi.rasa.com/simple``` in command prompt)

## How to run this chatbot in command prompt?

* First, run ```rasa train``` command to train the bot using the dataset provided in the repository.
* Then, use ```rasa shell``` to interact with chatbot in command prompt.
* Use ```rasa shell nlu``` to inspect the intent classified by the bot.

## How to run this chatbot with rasa-x?

* Run ```rasa run actions``` in one terminal. Do not close this tab.
* Now, run ```rasa x``` in another terminal. This will open a tab in the browser.

## How to test the chatbot?

* Run ```rasa test nlu --cross-validation``` to test the chatbot which uses nlu data to test.
* Run ```rasa test``` to test the chatbot with the test stories already provided in the ```tests/test_stories.yml``` file.
* After testing, you can find the results in the ```results``` directory.

## How to enable voice feature of the chatbot?

* Copy the ```voice_bot_gtts.py``` inside the ```actions``` folder.
* The instructions to activate this feature are already written inside this python file.
* Note: This feature currently only works through command line and also requires active internet connection for the ```gTTS``` library.
