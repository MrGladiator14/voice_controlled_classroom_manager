import speech_recognition as sr
import csv
from datetime import date

def recordAtt(recognizer):
    current_date = str(date.today())
    current_date += ".csv"
    print(current_date)

    data = [
        ['rollno', 'att'],
    ]

    for i in range(1, 5):
        row = []
        row.append(i)
        print("listening for roll no.", i)

        with sr.Microphone() as source:
            print("Attendance!")

            recognizer.energy_threshold = 4000

            audio3 = recognizer.listen(source)

            try:
                message = recognizer.recognize_google(audio3)

            except sr.UnknownValueError:
                print("Unable to recognize speech")

            except sr.RequestError as e:
                print("Error occurred during speech recognition:", str(e))

        if "present" in message:
            row.append(1)
        else:
            row.append(0)
        data.append(row)

    csv_file = current_date

    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("Attendance taken")
