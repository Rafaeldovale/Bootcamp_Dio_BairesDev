# Conversor de Imagens BMP
Este é um script simples e educacional em Python que converte imagens coloridas no formato BMP para tons de cinza ou para o formato binário (preto e branco puro). O principal objetivo do projeto é demonstrar a manipulação de pixels e o processamento de imagens sem a utilização de bibliotecas externas, usando apenas a biblioteca padrão do Python.

## Funcionalidades
    * **Conversão para Tons de Cinza:** Transforma a imagem em uma escala de 256 níveis de cinza (0-255).

    * **Conversão para Binário:** Converte a imagem para preto e branco puro (0 ou 255), usando um limiar de 128 como padrão.

    * **Independência de Bibliotecas:** O código é autossuficiente e não requer Pillow, OpenCV ou qualquer outra biblioteca externa.

## Por que apenas o formato BMP?
Este script foi intencionalmente projetado para funcionar sem o auxílio de bibliotecas externas. Por essa razão, ele opera exclusivamente com o formato **.bmp**.

## Como Usar:
    Pré-requisitos
        Python 3 instalado.

Passo a Passo
1.  **Salve o código:** Copie o código completo abaixo e salve-o em um arquivo chamado conversor.py.

2.  **Prepare a imagem:** Certifique-se de que a sua imagem original esteja no formato .bmp. Coloque-a na mesma pasta que o script conversor.py.

3.  **Execute a conversão:** Abra o terminal ou prompt de comando na pasta onde os arquivos estão salvos e execute um dos comandos abaixo:

    Para converter para Tons de Cinza:

        Bash

        python conversor.py cinza


    Para converter para Binário:

        Bash

        python conversor.py binario


Isso criará um novo arquivo na mesma pasta, com o sufixo _cinza.bmp ou _binario.bmp.