import datetime
from datetime import datetime as dt
import speech_recognition as sr
from createf import createf
from wa import wa
from openweb import openweb
from sendmail import sendmail
from recordAtt import recordAtt
from summary import summary

print("\t\t\t\t\tWelcome to My App")
print("\t\t\t\t\t-----------------")

print("""
        \t1. Note down
        \t2. Send a whatsapp message
        \t3. Open any website url
        \t4. Send an email
        \t5. Take Attendance
        \t6. Summary of Attendance 
    """)

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("\t\tWhat do you want to do?")

    recognizer.energy_threshold = 4000

    audio1 = recognizer.listen(source)

    try:
        ch = recognizer.recognize_google(audio1)

    except sr.UnknownValueError:
        print("Unable to recognize speech")

    except sr.RequestError as e:
        print("Error occurred during speech recognition:", str(e))

if ch == "1" or "file" in ch:
    createf(recognizer)

elif ch == "1" or "whatsapp" in ch or "message" in ch:
    wa(recognizer)

elif ch == "3" or 'website' in ch:
    openweb(recognizer)

elif ch == "6" or 'mail' in ch:
    sendmail(recognizer)
elif ch == "3" or 'attendance' in ch:
    recordAtt(recognizer)

elif ch == "3" or 'summary' in ch:
    summary()
