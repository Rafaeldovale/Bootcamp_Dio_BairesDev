import os
import cv2
import numpy as np
import pandas as pd
from mtcnn import MTCNN
from keras_facenet import FaceNet

# --- CONFIGURAÇÃO ---
DATASET_DIR = "dataset"
CSV_FILE = "embeddings.csv"

# --- INICIALIZAÇÃO DOS MODELOS ---
# O modelo padrão da sua biblioteca gera embeddings de 512 dimensões
detector_de_face = MTCNN()
facenet_model = FaceNet() # Não passe a chave 'v2' aqui

# --- FUNÇÕES AUXILIARES ---
def extrair_rosto(caminho_imagem):
    try:
        imagem_rgb = cv2.cvtColor(cv2.imread(caminho_imagem), cv2.COLOR_BGR2RGB)
        resultados_deteccao = detector_de_face.detect_faces(imagem_rgb)
        
        if len(resultados_deteccao) == 0:
            return None
        
        x, y, largura, altura = resultados_deteccao[0]['box']
        x1, y1 = abs(x), abs(y)
        x2, y2 = abs(x) + largura, abs(y) + altura
        
        rosto_extraido = imagem_rgb[y1:y2, x1:x2]
        rosto_redimensionado = cv2.resize(rosto_extraido, (160, 160))
        
        return rosto_redimensionado

    except Exception as e:
        print(f"Erro ao processar a imagem {caminho_imagem}: {e}")
        return None

def obter_embedding(rosto):
    rosto_expandido = np.expand_dims(rosto, axis=0)
    embedding = facenet_model.embeddings(rosto_expandido)
    return embedding[0]

# --- PROCESSO PRINCIPAL ---
def processar_dataset():
    lista_embeddings = []
    
    for nome_pasta in os.listdir(DATASET_DIR):
        caminho_pasta = os.path.join(DATASET_DIR, nome_pasta)
        
        if os.path.isdir(caminho_pasta):
            print(f"Processando a pasta: {nome_pasta}...")
            
            for nome_arquivo in os.listdir(caminho_pasta):
                caminho_completo_imagem = os.path.join(caminho_pasta, nome_arquivo)
                
                rosto = extrair_rosto(caminho_completo_imagem)
                
                if rosto is not None:
                    embedding = obter_embedding(rosto)
                    dados_linha = [nome_pasta] + list(embedding)
                    lista_embeddings.append(dados_linha)
                    print(f"  > Embedding gerado para {nome_arquivo}")

    # Cria as colunas para 512 embeddings
    colunas = ['pessoa'] + [f'emb_{i}' for i in range(512)]
    df_embeddings = pd.DataFrame(lista_embeddings, columns=colunas)
    df_embeddings.to_csv(CSV_FILE, index=False)
    
    print("\n--- Processo Concluído! ---")
    print(f"Embeddings salvos em '{CSV_FILE}'")
    print(f"Total de {len(df_embeddings)} embeddings salvos.")

if __name__ == '__main__':
    processar_dataset()