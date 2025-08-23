#  Descrição do Desafio
    Cálculo de Métricas de Avaliação de Aprendizado 

    Neste projeto, vamos calcular as principais métricas para avaliação de modelos de classificação de dados, como acurácia, sensibilidade (recall), especificidade, precisão e F-score. 


# Introdução
    Este projeto tem como objetivo construir, treinar e avaliar uma Rede Neural Convolucional (CNN) para a tarefa de classificação de imagens. O modelo é treinado no famoso conjunto de dados MNIST, que consiste em 70.000 imagens de dígitos manuscritos (de 0 a 9).

    O foco principal do projeto é a avaliação do desempenho do modelo. Após o treinamento, usamos uma matriz de confusão para calcular e analisar as principais métricas de classificação: Acurácia, Sensibilidade (Recall), Especificidade, Precisão e F1-Score.

# Arquitetura do Modelo
    O modelo é uma Rede Neural Convolucional sequencial, projetada para extrair características das imagens e classificá-las. Sua arquitetura é composta pelas seguintes camadas:

    *Camadas de Convolução (Conv2D)*: Extraem características como bordas e texturas.

    *Camadas de Max Pooling (MaxPooling2D):* Reduzem a dimensão das imagens, o que ajuda a controlar o número de parâmetros.

    *Camada de Achatamento (Flatten)*: Converte a matriz 2D de características em um vetor 1D.

    *Camadas Densely Conectadas (Dense)*: A camada final de classificação, onde a camada de saída usa a função de ativação softmax para prever a probabilidade de cada dígito.

# Métricas de Avaliação
    As seguintes métricas são calculadas a partir da matriz de confusão para fornecer uma avaliação completa do desempenho do modelo:

    *Acurácia*: A proporção de previsões corretas sobre o total de previsões.

    *Sensibilidade (Recall)*: A capacidade do modelo de encontrar todas as amostras de uma classe positiva.

    *recisão*: A proporção de previsões positivas que foram realmente corretas.

    *Especificidade*: A capacidade do modelo de identificar corretamente as amostras negativas.

    *F1-Score*: A média harmônica entre precisão e sensibilidade, útil para avaliar o equilíbrio do modelo.

# Como Executar o Projeto
Certifique-se de ter as bibliotecas necessárias instaladas. Se não as tiver, instale-as usando pip:

## pip install tensorflow matplotlib numpy seaborn pandas
## Copie o código completo para um arquivo Python (por exemplo, main.py).

Execute o arquivo no seu terminal ou ambiente de desenvolvimento (Jupyter Notebook, Google Colab, etc.).

O programa irá baixar o conjunto de dados, treinar o modelo, imprimir a acurácia e o log de treinamento, e exibir um mapa de calor da matriz de confusão, além de imprimir as métricas calculadas.