Assistente Virtual 

Este projeto é um assistente virtual construído do zero em Python. Utilizando o Processamento de Linguagem Natural (PLN), o sistema é capaz de interagir com o usuário por meio de comandos de voz, entendê-los e executar ações automatizadas.

Recursos e Tecnologias
O projeto foi desenvolvido em Python e utiliza as seguintes bibliotecas para as suas funcionalidades:

pyttsx3: Para transformar texto em voz (Text-to-Speech), permitindo que o assistente responda ao usuário.

SpeechRecognition: Para converter a fala do usuário em texto (Speech-to-Text), que é o cérebro do assistente.

pywhatkit: Para automatizar tarefas, como a reprodução de vídeos no YouTube.

wikipedia: Para acessar e pesquisar informações na Wikipédia, um dos comandos do assistente.

webbrowser: Para abrir páginas da web, como a página inicial do YouTube.

Estrutura do Projeto
A organização do projeto é simples, com um único arquivo de código que contém toda a lógica:

/assistente_virtual/
|
|-- assistente_modulo.py
|-- README.md
|-- stt_modulo.py
|-- tts_modulo.py
Como Usar

1. Pré-requisitos (Instalação de Dependências)
Primeiro, você deve instalar todas as bibliotecas necessárias para o projeto. Abra o seu terminal e execute o comando abaixo:

Bash

pip install pyttsx3 SpeechRecognition pywhatkit wikipedia
Observação: No Windows, caso a instalação do SpeechRecognition falhe, você pode precisar instalar o PyAudio separadamente. Tente o seguinte:

Bash

pip install pipwin
pipwin install pyaudio

2. Executar o Assistente
Com as dependências instaladas, basta executar o script principal. Abra o seu terminal na pasta do projeto e use o comando:

Bash

python assistente.py
O assistente irá iniciar e se apresentar, e em seguida, ficará pronto para ouvir o seu comando.

3. Comandos de Voz
Diga um dos seguintes comandos para o assistente quando ele estiver "ouvindo":

"Olá": Para iniciar uma conversa e receber uma saudação.

"Tocar [nome da música]": Para tocar uma música ou vídeo no YouTube.

"Pesquisar [termo]": Para pesquisar um termo na Wikipedia.

"Abrir YouTube": Para abrir a página inicial do YouTube no seu navegador.

"Obrigado" ou "Parar" ou "Desligar": Para finalizar a execução do programa.