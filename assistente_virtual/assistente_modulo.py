import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
import time

engine = pyttsx3.init()

def falar(texto):
    print(f"Assistente: {texto}")
    engine.say(texto)
    engine.runAndWait()

# --- Módulo Speech-to-Text ---
def ouvir_comando():
 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Assistente: Estou ouvindo...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1) 
        audio = r.listen(source)

    try:
        print("Assistente: Processando...")
        comando = r.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {comando}")
        return comando.lower()
    except sr.UnknownValueError:
        print("Assistente: Desculpe, não consegui entender o áudio.")
        return ""
    except sr.RequestError as e:
        print(f"Assistente: Erro no serviço de reconhecimento; {e}")
        return ""


def executar_comando():
    
    comando = ouvir_comando()
    
    if "olá" in comando:
        falar("Olá. Como posso ajudar?")
        
    elif "tocar" in comando:
        musica = comando.replace("tocar", "")
        falar(f"Tocando {musica} no YouTube.")
        pywhatkit.playonyt(musica)
        
    elif "pesquisar" in comando:
        termo_busca = comando.replace("pesquisar", "")
        falar(f"Procurando por {termo_busca} na Wikipedia.")
        wikipedia.set_lang("pt")
        try:
            resultado = wikipedia.summary(termo_busca, sentences=2)
            falar("A Wikipedia diz:")
            falar(resultado)
        except wikipedia.exceptions.PageError:
            falar("Não encontrei resultados para a sua pesquisa.")
        
    elif "abrir youtube" in comando:
        falar("Abrindo YouTube.")
        webbrowser.open("https://www.youtube.com")
        
    elif "obrigado" in comando:
        falar("De nada. Estou aqui para ajudar!")
        return True
    
    elif "parar" in comando or "desligar" in comando:
        falar("Desligando o assistente. Até mais!")
        return True


if __name__ == "__main__":
    falar("Olá, meu nome é Caroline. Estou pronta para ajudar.")
    while True:
        parar_execucao = executar_comando()
        if parar_execucao:
            break
        time.sleep(1)