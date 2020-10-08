import pyttsx3
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
volume=engine.getProperty("volume")
rate=engine.getProperty("rate")
engine.setProperty("voice",voices[1])
engine.setProperty("volume",volume-0.1)
engine.setProperty("rate",rate-20)

def  speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    speak("vikas is a good boy")    
