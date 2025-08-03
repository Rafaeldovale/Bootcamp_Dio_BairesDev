Classificador de Gatos e Cachorros com Transfer Learning

Este projeto demonstra a criação e o treinamento de um modelo de Deep Learning para classificar imagens de cães e gatos, utilizando a técnica de Transfer Learning com o modelo pré-treinado MobileNetV2. O desenvolvimento foi realizado no ambiente Google Colab, facilitando o acesso a recursos de GPU.


🚀 Como o Projeto Funciona
O projeto segue um fluxo de trabalho padrão para problemas de classificação de imagens:

1 - Download do Dataset: O conjunto de dados de Gatos vs. Cachorros foi baixado do Kaggle utilizando a biblioteca kagglehub, o que garantiu a obtenção de mais de 10.000 imagens de alta qualidade.

2 - Pré-processamento de Dados: Utilizamos o ImageDataGenerator do Keras para ler as imagens diretamente dos diretórios, aplicando normalização e técnicas de aumento de dados (data augmentation), como rotações e zooms, para tornar o modelo mais robusto.

3 - Transfer Learning: Em vez de treinar um modelo do zero, adotamos uma abordagem de Transfer Learning. Isso envolveu a utilização do modelo MobileNetV2, que já foi pré-treinado em milhões de imagens (no dataset ImageNet), e a adaptação de suas camadas finais para a nossa tarefa específica. As camadas do modelo base foram congeladas para preservar o conhecimento adquirido.

4 - Treinamento: O modelo foi treinado em 10 épocas, com um desempenho de alta acurácia, demonstrando a eficácia da abordagem de Transfer Learning.

5 - Teste e Validação: O modelo foi testado com imagens que ele nunca viu antes para comprovar sua capacidade de generalização.


🛠️ Tecnologias Utilizadas
. Google Colab: Ambiente de desenvolvimento para execução do código.

. TensorFlow / Keras: Frameworks de Deep Learning para construção e treinamento do modelo.

. MobileNetV2: Modelo pré-treinado usado para Transfer Learning.

. Kaggle Hub: Biblioteca para download e gerenciamento de datasets do Kaggle.

. Numpy: Biblioteca para manipulação de arrays numéricos.

. Matplotlib: Biblioteca para visualização de dados (exibição das imagens e previsões).


📂 Estrutura do Código
1 - O projeto está contido em um único notebook (.ipynb), seguindo a estrutura lógica:

2 - Configuração e Download: Instalação das bibliotecas e download do dataset do Kaggle.

3 - Carregamento e Pré-processamento: Configuração do ImageDataGenerator para os dados de treino e teste.

4 - Modelo e Treinamento: Definição do modelo MobileNetV2 com as camadas adicionais, compilação e treinamento.

Avaliação e Teste: Código para testar o modelo com imagens do conjunto de teste, exibindo a previsão.

🔗 Como Executar

1 - Abra o notebook ([nome_do_seu_notebook].ipynb) no Google Colab.

2 - Carregue sua chave da API do Kaggle (kaggle.json).

3 - Execute cada célula do notebook em ordem.

4 - Na última célula, você pode alterar o nome da imagem de teste (image_path) para testar outras imagens do dataset.

👨‍💻 Autor
[Rafael / @Rafaeldovale]

