import speech_recognition as sr

def createf(recognizer):
    with sr.Microphone() as source:
        print("Listening for notes...")

        recognizer.energy_threshold = 4000

        audio1 = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio1)
            print("Recognised Audio : ", text)
            print("What would you like to name this note..")

            recognizer.energy_threshold = 4000

            audio2 = recognizer.listen(source)

            try:
                fname = recognizer.recognize_google(audio2)
                file = open(fname + ".pdf", "w")
                file.write(text)
                file.close()
                print("File created successfully.")
            except sr.UnknownValueError:
                print("Unable to recognize speech")
            except sr.RequestError as e:
                print("Error occurred during speech recognition:", str(e))

        except sr.UnknownValueError:
            print("Unable to recognize speech")
        except sr.RequestError as e:
            print("Error occurred during speech recognition:", str(e))
