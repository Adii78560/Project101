import pyttsx3

def speak(text, voice_id):
    engine = pyttsx3.init(driverName='sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id)
    engine.say(text)
    engine.runAndWait()

# Rest of your code...
