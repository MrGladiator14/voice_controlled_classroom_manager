import smtplib
import speech_recognition as sr

def sendmail(recognizer):
    sender_email #= "sender@gmail.com"
    sender_password #= "ipbafsugmgkwcotw"
    receiver_email = input("Enter receiver email:")
    subject = "Demo"

    with sr.Microphone() as source:
        print("What is your message?")

        recognizer.energy_threshold = 4000

        audio3 = recognizer.listen(source)

        try:
            message = recognizer.recognize_google(audio3)

        except sr.UnknownValueError:
            print("Unable to recognize speech")

        except sr.RequestError as e:
            print("Error occurred during speech recognition:", str(e))

    def send_email(sender_email, sender_password, receiver_email, subject, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        email_message = f"Subject: {subject}\n\n{message}"

        server.sendmail(sender_email, receiver_email, email_message)

        server.quit()

        print("Email sent successfully!")

    send_email(sender_email, sender_password, receiver_email, subject, message)
