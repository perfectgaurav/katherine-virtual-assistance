import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import smtplib
my_email = "gauravkaushik035@gmail.com"
my_password = "monstercr7"
to_add="reciver email"

# ********* module to use voices built in windows********************
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# speak("gaurav is a genius")


def wishme():
    hour = int(datetime.datetime.now().hour)
    # print(hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning,,sir....This is Katherine...Your  virtual assistant.......How can i help you")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon,,sir....This is Katherine...your virtual assistant.........How can i help you")
    else:
        speak("Good Evening,,sir....This is Katherine...your virtual assistant......How can i help you")


# ********this function takes command through microphn and converting it into string**********
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-ssssin')
        print(f'user said:{query}')
    except Exception as e:
        print('Say that again please...')
        return 'None'
    return query


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_add,
            msg="subject:Automatic email generation\n\nThis is auto generated email."

        )


wishme()
query = takecommand().lower()
if 'wikipedia' in query:
    speak('searching wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("according to wikipedia")
    speak(results)
elif 'open youtube' in query:
    webbrowser.open("youtube.com")
elif 'open google' in query:
    webbrowser.open("google.com")
elif 'send email' in query:
    send_email()
