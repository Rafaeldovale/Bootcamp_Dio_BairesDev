Reconhecimento Facial: Projeto Friends

    Este projeto demonstra um sistema de reconhecimento facial simples, capaz de detectar e identificar membros do elenco da série "Friends" em uma foto de grupo. O sistema utiliza técnicas de deep learning para converter rostos em representações numéricas únicas (embeddings) e, em seguida, compará-las para fazer o reconhecimento.

Recursos e Tecnologias

    O projeto foi desenvolvido em Python e utiliza as seguintes bibliotecas e modelos:

    # mtcnn: Modelo de rede neural para detecção de múltiplos rostos em uma imagem.

    # keras-facenet: Modelo pré-treinado que converte rostos em vetores de 512 dimensões (embeddings).

    # opencv-python: Para carregar, processar e exibir imagens.

    # pandas: Para criar e gerenciar o arquivo CSV com o banco de dados de embeddings.

    # numpy: Para manipulação eficiente de dados numéricos.

Estrutura do Projeto

    O projeto segue uma estrutura de pastas simples para organizar o código e os dados.

    /nome_do_seu_projeto/
    |
    |-- gerar_embedding.py            # Script para criar o banco de dados (embeddings.csv)
    |-- reconhecer_simples.py         # Script para reconhecer rostos em uma nova foto
    |-- embeddings.csv                # Banco de dados com os embeddings gerados (criado após o passo 2)
    |-- foto_grupo.jpg                # Foto de grupo para teste
    |
    |-- /dataset/                     # Pasta com as fotos de referência
        |
        |-- /nome_do_personagem_1/    # Subpasta com as fotos individuais
        |   |-- foto_1.jpg
        |   |-- foto_2.jpg
        |
        |-- /nome_do_personagem_2/
        |   |-- foto_1.jpg
        |   |-- foto_2.jpg
        |-- etc...


Como Usar
    1. Pré-requisitos
    Certifique-se de ter o Python instalado e as seguintes bibliotecas:

    Bash

    pip install mtcnn
    pip install keras-facenet
    pip install opencv-python
    pip install numpy
    pip install pandas
    2. Preparar o Banco de Dados (Dataset)
    Crie a pasta dataset e, dentro dela, crie subpastas com o nome de cada personagem. Coloque pelo menos duas fotos de cada um dentro de sua respectiva pasta.

    3. Gerar os Embeddings
    Execute o script gerar_embedding.py. Este processo pode levar alguns minutos.

    Bash

    python gerar_embedding.py
    Ao final, um arquivo chamado embeddings.csv será gerado, contendo os embeddings (a "impressão digital" numérica) de cada rosto.

    4. Reconhecer os Rostos
    Edite o script reconhecer_simples.py para garantir que o nome da sua foto de grupo esteja correto.

    Python

    # No início do arquivo reconhecer_simples.py
    FOTO_TESTE = "friends_grupo.jpg" # Mude para o nome da sua foto de teste
    Em seguida, execute o script:

    Bash

    python reconhecer_simples.py
    O script irá gerar uma nova imagem chamada friends_resultado.jpg com os rostos detectados e identificados.

Créditos
    Agradecimentos à comunidade de código aberto e aos criadores das bibliotecas MTCNN e Keras-FaceNet, que tornaram este projeto possível.