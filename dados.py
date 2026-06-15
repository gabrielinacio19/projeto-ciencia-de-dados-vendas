# ========================================
# ARQUIVO DE DADOS - dados.py
# ========================================
# Esse arquivo lê a base de vendas

import pandas as pd  # Para ler e trabalhar com dados em tabela
import os           # Para mexer com arquivos e pastas

def carregar_dados():
    """
    Lê o arquivo CSV e devolve os dados em um DataFrame.
    """
    print("Carregando dados...")
    
    # Monta o caminho do arquivo da base
    path = os.path.join("data", "sales_data.csv")
    
    # Confere se o arquivo existe
    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo de dados não encontrado em: {path}")
    
    try:
        # Lê o CSV e guarda em um DataFrame
        df = pd.read_csv(path)
        print("Dados carregados. Linhas:", len(df))
        # Mostra as primeiras linhas só para conferir
        print(df.head())
        return df
    except Exception as e:
        print(f"Erro lendo o arquivo CSV: {e}")
        raise