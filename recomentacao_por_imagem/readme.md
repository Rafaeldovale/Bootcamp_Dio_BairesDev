Sistema de Recomendação por Imagens

Este projeto demonstra um sistema de recomendação baseado em similaridade visual. Em vez de usar dados textuais (preço, marca, modelo), o sistema analisa a aparência física dos produtos para recomendar itens que são visualmente semelhantes em termos de cor, formato e textura.

Recursos e Tecnologias
O projeto utiliza bibliotecas de deep learning e de processamento de dados em Python:

TensorFlow & Keras: Para carregar e usar o modelo VGG16, que extrai as características visuais das imagens.

Pillow: Para manipular e processar as imagens antes de serem passadas para o modelo.

NumPy: Para lidar com os vetores numéricos de alta dimensão (os embeddings).

Pandas: Para gerenciar os dados dos embeddings e salvá-los em um arquivo CSV.

scikit-learn: Para calcular a similaridade entre os embeddings e encontrar os produtos mais parecidos.

Estrutura do Projeto
O projeto é organizado com a seguinte estrutura de arquivos:

/nome_do_seu_projeto/
|
|-- gerar_embeddings_imagens.py     # Script para criar o banco de dados de embeddings
|-- recomendador_imagens.py         # Script para recomendar produtos visualmente similares
|-- embeddings_imagens.csv          # Banco de dados com os embeddings (criado após o passo 2)
|-- /produtos/                      # Pasta com as imagens dos produtos

1. Pré-requisitos
Primeiro, instale todas as bibliotecas necessárias. Abra seu terminal e execute:

Bash

pip install tensorflow keras Pillow numpy pandas scikit-learn
2. Preparar as Imagens
Crie uma pasta chamada produtos na mesma localização dos seus scripts. Dentro dessa pasta, coloque as imagens dos produtos que você quer usar no seu sistema de recomendação.

3. Gerar os Embeddings
Este passo irá criar o banco de dados numérico do seu projeto. Execute o script gerar_embeddings_imagens.py.

Bash

python gerar_embeddings_imagens.py
Ao final do processo, um arquivo chamado embeddings_imagens.csv será criado, contendo a "impressão digital" numérica de cada imagem.

4. Criar o Sistema de Recomendação

5. Executar o Recomendador
Execute o script recomendador_imagens.py para ver os resultados.

Bash

python recomendador_imagens.py