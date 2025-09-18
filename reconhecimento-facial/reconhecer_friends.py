import cv2
import numpy as np
import pandas as pd
from mtcnn import MTCNN
from keras_facenet import FaceNet
from scipy.spatial.distance import euclidean

# --- CONFIGURAÇÃO ---
# Coloque aqui o nome da foto de grupo que você quer testar
FOTO_TESTE = "friends.jpg"

# Limiar de reconhecimento:
# Distâncias menores que este valor indicam que é a mesma pessoa.
LIMIAR_RECONHECIMENTO = 12.0

# --- PREPARAÇÃO ---
# Inicializa os modelos
detector_de_face = MTCNN()
facenet_model = FaceNet()

# Carrega todos os embeddings do arquivo CSV
try:
    df = pd.read_csv("embeddings.csv")
    nomes_conhecidos = df['pessoa'].values
    embeddings_conhecidos = df.drop(columns='pessoa').values
except FileNotFoundError:
    print("Erro: 'embeddings.csv' não encontrado. Certifique-se de ter executado o 'gerar_embeddings.py'.")
    exit()

def obter_embedding(rosto):
    """Gera o embedding de um rosto usando o modelo FaceNet."""
    rosto_expandido = np.expand_dims(rosto, axis=0)
    embedding = facenet_model.embeddings(rosto_expandido)
    return embedding[0]

# --- PROCESSO DE RECONHECIMENTO ---
# Carrega a imagem que será analisada
imagem = cv2.imread(FOTO_TESTE)
if imagem is None:
    print(f"Erro: Não foi possível carregar a imagem '{FOTO_TESTE}'.")
    exit()

imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# Detecta todos os rostos na imagem
rostos_detectados = detector_de_face.detect_faces(imagem_rgb)

print(f"Total de {len(rostos_detectados)} rostos encontrados na foto de grupo.")

# Loop para cada rosto detectado
for resultado in rostos_detectados:
    x, y, largura, altura = resultado['box']
    x1, y1, x2, y2 = abs(x), abs(y), x + largura, y + altura
    
    rosto_extraido = imagem_rgb[y1:y2, x1:x2]
    rosto_redimensionado = cv2.resize(rosto_extraido, (160, 160))
    
    # Obtém o embedding do rosto detectado
    embedding_detectado = obter_embedding(rosto_redimensionado)

    # --- RECONHECIMENTO ---
    # Encontra o embedding mais próximo no seu banco de dados
    menor_distancia = float('inf')
    nome_identificado = "Desconhecido"

    for i, embedding_conhecido in enumerate(embeddings_conhecidos):
        distancia = euclidean(embedding_conhecido, embedding_detectado)
        
        if distancia < menor_distancia:
            menor_distancia = distancia
            nome_identificado = nomes_conhecidos[i]
            
    # Verifica se a menor distância está abaixo do limiar
    if menor_distancia > LIMIAR_RECONHECIMENTO:
        nome_identificado = "Desconhecido"
    
    print(f"  > Rosto identificado como: {nome_identificado} (Distância: {menor_distancia:.2f})")
    
    # --- VISUALIZAÇÃO ---
    cor = (0, 255, 0) if nome_identificado != "Desconhecido" else (0, 0, 255)
    cv2.rectangle(imagem, (x1, y1), (x2, y2), cor, 2)
    cv2.putText(imagem, nome_identificado, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, cor, 2)

# Salva a imagem com os resultados
cv2.imwrite("friends_resultado.jpg", imagem)
print("\nProcesso concluído! A imagem 'friends_resultado.jpg' foi salva.")