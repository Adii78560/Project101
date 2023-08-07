import speech_recognition as sr
from gtts import gTTS
import os

# Import pyaudio and try using it for audio input
import pyaudio
pa = pyaudio.PyAudio()
device_index = 0  # Try different device indices until you find the right one
with sr.Microphone(device_index=device_index) as source:
    # Your existing code here...

# audio = recognizer.listen(source)
# print(audio)  # Add this line for debugging

# # Import pyaudio and try using it for audio input
# import pyaudio
# pa = pyaudio.PyAudio()
# device_index = 0  # Try different device indices until you find the right one
# with sr.Microphone(device_index=device_index) as source:
#     # Your existing code here...


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print(f"An error occurred while processing your request: {e}")

    return ""


def speak(text, voice_id):
    # Your existing speak() function remains unchanged

def main():
    print("Hello! I am your virtual assistant.")
    print("Press 'Q' or say 'exit' to quit.")

    while True:
        user_input = listen()

        if user_input == "q" or user_input == "exit":
            print("Goodbye! Exiting the virtual assistant.")
            break

        # Here you can add your logic to respond to user commands.
        response = "Sorry, I'm still learning. I can't help with that yet."
        speak(response, voice_id=1)  # Use 1 for female voice, 0 for male voice.

if __name__ == "__main__":
    main()
