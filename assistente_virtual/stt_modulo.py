import speech_recognition as sr
import time

def ouvir_comando():
    """
    Usa o microfone para ouvir um comando e retorna o texto.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Assistente: Estou ouvindo...")
        # Adiciona um tempo para o reconhecedor se ajustar ao ruído ambiente.
        r.pause_threshold = 1
        # O reconhecedor vai ajustar a sensibilidade do microfone.
        r.adjust_for_ambient_noise(source, duration=1) 
        audio = r.listen(source)

    try:
        print("Assistente: Processando...")
        # Usa o Google Web Speech API para reconhecer a fala.
        comando = r.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {comando}")
        return comando.lower()
    except sr.UnknownValueError:
        print("Assistente: Desculpe, não consegui entender o áudio.")
        return ""
    except sr.RequestError as e:
        print(f"Assistente: Erro no serviço de reconhecimento; {e}")
        return ""


if __name__ == "__main__":
    ouvir_comando()