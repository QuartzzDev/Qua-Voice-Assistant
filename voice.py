import speech_recognition as sr
from gtts import gTTS
import os
import threading
import time
import datetime

def recognize_speech():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Sizi dinliyorum, bir komut verin...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio, language="tr-TR")  # Türkçe için dil kodu "tr-TR"
            print("Söylediğiniz komut: " + command)
            return command
        except sr.UnknownValueError:
            print("Anlayamadım, tekrarlayın.")
            return ""
        except sr.RequestError as e:
            print("Ses tanıma servisine ulaşılamadı; {0}".format(e))
            return ""

def text_to_speech(text):
    tts = gTTS(text=text, lang="tr")  # Türkçe için dil kodu "tr"
    tts.save("response.mp3")
    os.system("start response.mp3")

def process_commands():
    while True:
        command = recognize_speech()

        if "merhaba" in command.lower():
            response = "Merhaba! Size nasıl yardımcı olabilirim?"
            text_to_speech(response)
            time.sleep(1)
        elif "nasılsın" in command.lower():
            response = "İyiyim, siz nasılsınız?"
            text_to_speech(response)
            time.sleep(1)
        elif "güle güle" in command.lower():
            response = "Güle güle, hoşçakalın!"
            text_to_speech(response)
            break
        elif "isminiz ne" in command.lower():
            response = "Merhaba ben Quartzz Sesli Asistan, Size nasıl yardımcı"
            text_to_speech(response)
            time.sleep(1)
        elif "teşekkür ederim" in command.lower():
            response = "Rica ederim, size yardımcı olabildiysem ne mutlu bana!"
            text_to_speech(response)
            time.sleep(1)
        elif "ne yapıyorsun" in command.lower():
            response = "Ben Quartzz Sesli Asistan , size yardımcı olmak için buradayım. Sormak istediğiniz bir şey var mı?"
            text_to_speech(response)
            time.sleep(1)
            if "var" in command.lower():
                response = "Tabi Sizi Dinliyorum ."
                text_to_speech(response)
                time.sleep(1)
        elif "saat kaç" in command.lower():
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M")
            response = "The current time is " + current_time
            text_to_speech(response)
            time.sleep(1)
        elif "teşekkürler" in command.lower():
            response = "Rica ederim, size yardımcı olabildiysem ne mutlu bana!"
            text_to_speech(response)
            time.sleep(1)
        else:
            response = "Anlayamadım, tekrar eder misiniz?"
            text_to_speech(response)
            time.sleep(1)

if __name__ == "__main__":
    command_thread = threading.Thread(target=process_commands)
    command_thread.start()
    command_thread.join()
