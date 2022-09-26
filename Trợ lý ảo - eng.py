import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
from random import randint
recognizer = sr.Recognizer()

robot_brain = ""
def speak(text):
        tts = gTTS(text=text, lang='en-us')
        filename = 'voice.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)

def nghe():
    you = " "
    with sr.Microphone() as mic:
        print("Loại bỏ tiếng ồn ")
        recognizer.adjust_for_ambient_noise(mic, duration=1)
        print('Tôi đang nghe bạn đây...')
        recorded_audio = recognizer.listen(mic, timeout=4)
        print("Done recording")

        try:
            print("Recognizing the text")
            you = recognizer.recognize_google(recorded_audio, language="en-us")
            print("You:", you)

        except Exception as ex:
            you = "Mời bạn nói lại"
    
    return you



while True:

    you = nghe()

    if you in "Who is handsome": 
        robot_brain = "You is very handsome"
    elif you in "Xin chào": 
        robot_brain = "Chào Quốc. Tôi là trợ lý ảo"
    elif you in "Hôm nay là thứ mấy": 
        robot_brain = "Hôm nay là thứ hai"
    elif you in "Tổng thống hiện tại của Mỹ là ai ?":
        robot_brain = "Là tổng thống Biden"
    elif you in "chơi trò chơi":
        robot_brain = "Cùng chơi búa kéo bao"
        speak(robot_brain)
        while True:
            speak("Lựa chọn của bạn: ")
            you = nghe()
            if you in "Dừng trò chơi": 
                break
            robot =  randint(0,2)
            if robot == 0: robot = "Búa"
            elif robot == 1: robot ="Kéo"
            else: robot = "Bao"
            
            if you == "búa":
                if robot == "Bao": robot_brain = "Bạn thua."
                elif robot == "Kéo": robot_brain = "Bạn thắng. Bạn giỏi vãi lồn"
                else: robot_brain = "Hoà"

            print('Robot: ', robot_brain )
            speak(robot_brain)
        continue
        
    elif you in "tạm biệt": 
        robot_brain = "Tạm biệt bạn"
        print("Robot: ", robot_brain)
        speak(robot_brain)
        break
    else: 
        robot_brain = "Please speak again"

    print('Robot: ', robot_brain )
    speak(robot_brain)