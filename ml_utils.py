# ========================================
# UTILITÁRIOS DE MACHINE LEARNING
# ========================================
# Funções auxiliares para os modelos preditivos e prescritivos.

import os
import pandas as pd


def garantir_output():
    """Garante que a pasta output exista antes de salvar gráficos."""
    os.makedirs("output", exist_ok=True)


def carregar_base():
    """Lê a base de vendas e devolve um DataFrame."""
    path = os.path.join("data", "sales_data.csv")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo de dados não encontrado em: {path}")
    return pd.read_csv(path)


def normalizar_colunas(df):
    """Cria uma versão padronizada dos nomes das colunas para facilitar o uso nos modelos."""
    mapa = {
        "Sales_Amount": "Sales_Value",
        "Quantity_Sold": "Quantity_Sold",
        "Unit_Cost": "Unit_Cost",
        "Unit_Price": "Unit_Price",
        "Product_Category": "Product_Category",
        "Region": "Region",
        "Sales_Rep": "Sales_Rep",
        "Customer_Type": "Customer_Type",
    }
    renomear = {col: novo for col, novo in mapa.items() if col in df.columns}
    return df.rename(columns=renomear).copy()


def preparar_dados_ml(df):
    """Padroniza a base e devolve somente as colunas importantes para os novos modelos."""
    df = normalizar_colunas(df)
    df["Alta_Venda"] = (df["Sales_Value"] > df["Sales_Value"].median()).astype(int)
    return df
