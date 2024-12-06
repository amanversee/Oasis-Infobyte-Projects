import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to make Jarvis speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet the user
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis. Please tell me how may I help you.")

# Function to take voice input from the user
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)   #Added for better noise handling
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Fixed method
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again, please...")
        return "None"
    return query

# Main program
if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        if query == "none":
            continue

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")  # Fixed case
            try:
                results = wikipedia.summary(query, sentences=2)  # Fixed argument
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak("Sorry, I couldn't find anything on Wikipedia.")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open folder' in query:
            folderpath = "cC:\\aman programming\\Info byte"
            if os.path.exists(folderpath):
                os.startfile(folderpath)
            else:
                speak("Sorry the folder path does not exist.")
        elif 'exit the program' in query:
            speak("Signing off....thank you!")
            exit()
