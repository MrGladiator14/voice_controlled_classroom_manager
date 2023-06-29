import webbrowser
import speech_recognition as sr

def openweb(recognizer):
    with sr.Microphone() as source:
        print("Which website you want to open?")

        recognizer.energy_threshold = 4000

        audio2 = recognizer.listen(source)

        try:
            name = recognizer.recognize_google(audio2)
            url = "https://" + name + ".com"
            webbrowser.open(url)

        except sr.UnknownValueError:
            print("Unable to recognize speech")

        except sr.RequestError as e:
            print("Error occurred during speech recognition:", str(e))
