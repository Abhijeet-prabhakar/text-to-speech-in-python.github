import pyaudio as pa
import pyttsx3


engine = pyttsx3.init()

user_input = input("What to want to speak: ")
voices = engine.getProperty('voices')
a = input("Press enter to exit")

# print(voices)
# print(voices[0])
# print(voices[1])

engine.say(user_input)
engine.runAndWait()
engine.stop()
