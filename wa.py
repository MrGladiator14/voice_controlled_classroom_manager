import datetime
from datetime import datetime as dt
import pywhatkit
import speech_recognition as sr

def wa(recognizer):
    no = input("Enter 10 Digit number : ")
    no = "+91" + no
    with sr.Microphone() as source:
        print("What is your message?")

        recognizer.energy_threshold = 4000

        audio2 = recognizer.listen(source)

        try:
            message = recognizer.recognize_google(audio2)

        except sr.UnknownValueError:
            print("Unable to recognize speech")

        except sr.RequestError as e:
            print("Error occurred during speech recognition:", str(e))
    time = dt.now().time()
    hr = time.hour
    min = time.minute
    pywhatkit.sendwhatmsg(no, message, hr, min + 2)
