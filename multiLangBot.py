# importing speech recognition package from google api
from fnmatch import translate
import speech_recognition as sr
import playsound  # to play saved mp3 file
from gtts import gTTS  # google text to speech
import os  # to save/open files
from googletrans import Translator, constants

num = 1


def assistant_speaks(output):
    global num

    # num to rename every audio file
    # with different name to remove ambiguity
    output = language_translator_botToPerson(output)
    num += 1
    print("Bot : ", output)

    toSpeak = gTTS(text=output, lang='hi', slow=False)

    # saving the audio file given by google text to speech
    file = 'C:\\Praneetha\\voice3.mp3'
    toSpeak.save(file)
    # print(file)

    # playsound package is used to play the audio file.
    playsound.playsound("C:\\Praneetha\\voice3.mp3", True)
    os.remove(file)


def get_audio():

    while(True):
        rObject = sr.Recognizer()
        audio = ''

        with sr.Microphone() as source:
            print("Speak...")

            # recording the audio using speech recognition
            audio = rObject.listen(source, phrase_time_limit=5)
        print("Stop.")  # limit 5 secs

        try:
            text = rObject.recognize_google(audio, language='en-US')
            print("Person : ", text)
            return text
        except:
            assistant_speaks(
                "Could not understand your audio, PLease try again !")
            return get_audio()
            # return 0


# language_translator_personToBot method is used to translate the person's language
# instructions to Bot understandable/default language.
def language_translator_personToBot(text):
    translator = Translator()

    translation = translator.translate(text, dest="en")
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


# language_translator_botToPerson method is used to translate Bot instructions to person's preferred language.
def language_translator_botToPerson(text):
    translator = Translator()

    translation = translator.translate(text, dest="hi")
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
    return translation.text


# Driver Code
if __name__ == "__main__":
    text = get_audio()
    language_translator_botToPerson(text)

    assistant_speaks("Welcome to Amaara restaurant")
    assistant_speaks("May I know your name")

    name = get_audio()
    assistant_speaks("Hello " + name + " ,Hope you are doing well")

    assistant_speaks("what would you like to order?")
    text = get_audio().lower()
    assistant_speaks("Ordered items are " + text)

    assistant_speaks(
        "Please tell your mobile number to proceed with order confirmation")
    mobileNumber = get_audio()

    assistant_speaks(
        'Please do the payment through the link sent to your mobile.')
    assistant_speaks('Your order is placed and the order number is 101.')
