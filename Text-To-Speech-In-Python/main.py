# modules
import pyaudio
import speech_recognition as s_r
import pyttsx3

# variable
mic = s_r.Microphone()
rec = s_r.Recognizer()

# print(s_r.__version__)
# print(s_r.Microphone.list_microphone_names())

# main speech engine
def Sp(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# mega shutdown process
# loop
    while True:
        try:
            with mic as source:
            
                rec.adjust_for_ambient_noise(source, duration=0.1)
                audio = rec.listen
                txt = rec.recognize_google(audio)
                txt = txt.lower()
                print(txt)
                print("It Works")
        
        except s_r.RequestError as e:
             print("Could not request results; {0}".format(e))
        break

endput = input("Type quit to quit the program")
if endput == "quit":
       quit()

