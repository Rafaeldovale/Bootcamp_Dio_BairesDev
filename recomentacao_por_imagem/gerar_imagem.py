import os
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input


# Nome da pasta com todas as suas imagens
IMAGEM_DIR = "produtos"

# Nome do arquivo CSV que será gerado
CSV_FILE = "embeddings_imagens.csv"

modelo_vgg = VGG16(weights='imagenet', include_top=False, pooling='avg')

def extrair_embedding(caminho_imagem):
    """
    Carrega a imagem, a pré-processa e extrai o embedding usando o VGG16.
    """
    try:
        img = image.load_img(caminho_imagem, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array_expandido = np.expand_dims(img_array, axis=0)
        img_preprocessada = preprocess_input(img_array_expandido)
        
        embedding = modelo_vgg.predict(img_preprocessada)
        
        return embedding.flatten() 

    except Exception as e:
        print(f"Erro ao processar a imagem {caminho_imagem}: {e}")
        return None

# --- PROCESSO PRINCIPAL ---
def processar_imagens():
    """
    Percorre o diretório de imagens, extrai embeddings e salva no CSV.
    """
    lista_embeddings = []
    
    if not os.path.isdir(IMAGEM_DIR):
        print(f"Erro: O diretório '{IMAGEM_DIR}' não foi encontrado.")
        return

    for nome_arquivo in os.listdir(IMAGEM_DIR):
        caminho_completo = os.path.join(IMAGEM_DIR, nome_arquivo)
        
        if os.path.isfile(caminho_completo):
            print(f"Processando a imagem: {nome_arquivo}...")
            
            embedding = extrair_embedding(caminho_completo)
            
            if embedding is not None:
                lista_embeddings.append([nome_arquivo] + list(embedding))
                print(f"  > Embedding gerado.")

    num_embeddings = len(lista_embeddings)
    if num_embeddings > 0:
        colunas = ['imagem'] + [f'emb_{i}' for i in range(len(lista_embeddings[0]) - 1)]
        df_embeddings = pd.DataFrame(lista_embeddings, columns=colunas)
        df_embeddings.to_csv(CSV_FILE, index=False)
        
        print("\n--- Processo Concluído! ---")
        print(f"Embeddings salvos em '{CSV_FILE}'")
        print(f"Total de {len(df_embeddings)} embeddings salvos.")
    else:
        print("\n--- Processo Concluído, mas nenhum embedding foi gerado. ---")

if __name__ == '__main__':
    processar_imagens()