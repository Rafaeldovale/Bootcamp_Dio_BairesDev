import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

CSV_FILE = "embeddings_imagens.csv"

def recomendar_por_imagem(nome_imagem, num_recomendacoes=5):
    """
    Carrega os embeddings, encontra a imagem de entrada e recomenda as mais similares.
    """
    try:
        df = pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        return "Erro: Arquivo de embeddings não encontrado. Rode 'gerar_embeddings_imagens.py' primeiro."

    if nome_imagem not in df['imagem'].values:
        return f"Erro: Imagem '{nome_imagem}' não encontrada no banco de dados."

    indice_imagem = df.index[df['imagem'] == nome_imagem].tolist()[0]
    
    embedding_entrada = df.iloc[indice_imagem, 1:].values.reshape(1, -1)
    
    todos_embeddings = df.iloc[:, 1:].values
    
    similaridades = cosine_similarity(embedding_entrada, todos_embeddings).flatten()
    
    indices_similares = similaridades.argsort()[-num_recomendacoes-1:-1][::-1]
    
    nomes_recomendados = df.iloc[indices_similares]['imagem']
    
    return nomes_recomendados

imagem_de_entrada = "tenis.jpg" 

recomendacoes = recomendar_por_imagem(imagem_de_entrada, num_recomendacoes=5)

print(f"Se você gostou de '{imagem_de_entrada}', também pode gostar de:")
print(recomendacoes)