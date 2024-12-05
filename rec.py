import speech_recognition as sr
import webbrowser
import pyttsx3
# Initialize recognizer
recognizer = sr.Recognizer()

engine = pyttsx3.init()
engine.setProperty('rate', 200)  
engine.setProperty('volume', 1)
def listen_for_speech():
    with sr.Microphone() as source:
        print("Listening... Please speak")
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        return text.lower()  # Return the recognized text in lowercase for easier comparison
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return None
    except sr.RequestError as e:
        print(f"Request failed; {e}")
        return None

# Main loop to keep listening
while True:
    # Listen and get the speech
    speech_text = listen_for_speech()
    
    # If we recognize the word 'end  jarvis', stop the program
    
    
    li = ["google", "youtube", "facebook", "amazon", "twitter", "instagram", "wikipedia", "reddit", "linkedin", "netflix", "apple", "microsoft", "pinterest", "tumblr", "bbc", "cnn", "nike", "spotify", "twitch", "yahoo", "etsy", "quora", "stackoverflow", "vimeo", "snapchat", "dropbox", "salesforce", "airbnb", "zillow", "whatsapp", "skype", "national geographic", "aliexpress", "github", "medium", "yandex", "bing", "new york times"]

    if "hey jarvis" == speech_text:
            engine.say("My master how can i help u")
            engine.runAndWait()
    for check in li:
            fin="open "+check
            if fin in speech_text:
                text="opening"+check+".com"
                engine.say(text)
                webbrowser.open(check+".com")
                engine.runAndWait()
    if "thank you jarvis" in speech_text:
            engine.say("It was my pleasure helping you (My master)")  
            engine.runAndWait()  
            break   
