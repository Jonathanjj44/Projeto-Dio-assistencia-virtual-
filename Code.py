import speech_recognition as sr
import pyttsx3

# Inicializa o reconhecedor de fala
r = sr.Recognizer()

# Inicializa o sintetizador de voz
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Fale algo...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language='pt-BR')
            print("Você disse:", text)
            return text
        except sr.UnknownValueError:
            print("Não entendi")
        except sr.RequestError as e:
            print("Erro do serviço de reconhecimento de fala; {0}".format(e))

while True:
    text = listen()
    # Aqui você implementaria a lógica para processar o texto e executar as tarefas
