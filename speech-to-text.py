import speech_recognition as sr

recognizer = sr.Recognizer()


with sr.Microphone() as mic:
    print("Adjusting noise ")
    recognizer.adjust_for_ambient_noise(mic, duration=1)
    print("Recording for 4 seconds")
    recorded_audio = recognizer.listen(mic, timeout=4)
    print("Done recording")

''' Recorgnizing the Audio '''
try:
    print("Recognizing the text")
    text = recognizer.recognize_google(
            recorded_audio, 
            language="vi"  
        )
    print("Decoded Text : {}".format(text))

except Exception as ex:
    print(ex)