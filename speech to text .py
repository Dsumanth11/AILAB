# pip install speechrecognition
# pip install pyaudio
# sudo apt-get install python3-pyaudio
import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("please speak")
    audio=r.listen(source,timeout=10,phrase_time_limit=15)
    try:
        print("please wait while we are recognizing")
        text=r.recognize_google(audio)
        print(text)
    except:
        print("didn't Recognise")