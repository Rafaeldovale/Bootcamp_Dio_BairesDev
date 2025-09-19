"""
fazer as importações:
pip install pyttsx3
pip install SpeechRecognition
pip install pywhatkit
pip install wikipedia
"""


import pyttsx3

# Inicializa o motor de voz
engine = pyttsx3.init()

# Define a função para o assistente falar
def falar(texto):
    """
    Transforma texto em áudio e o reproduz.
    """
    print(f"Assistente: {texto}")
    engine.say(texto)
    engine.runAndWait()

# --- Exemplo de uso ---
if __name__ == "__main__":
    falar("Olá, eu sou o seu assistente virtual. Como posso ajudar?")
    falar("Vamos começar o nosso projeto.")