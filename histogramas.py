# ========================================
# ARQUIVO DE HISTOGRAMAS - histogramas.py
# ========================================
# Esse arquivo monta os histogramas do projeto

import matplotlib
matplotlib.use('Agg')  # Para salvar os gráficos sem abrir janela
import matplotlib.pyplot as plt  # Para criar os gráficos
import os  # Para trabalhar com pastas

def gerar_histogramas(df):
    """
    Gera 4 histogramas com os dados da base.
    """
    try:
        print("Gerando histogramas...")
        os.makedirs('output', exist_ok=True)  # Cria a pasta se precisar

        # Histograma da quantidade vendida
        if 'Quantity_Sold' in df.columns:
            plt.figure(figsize=(8,5))
            df['Quantity_Sold'].hist()
            plt.title("Distribuição da Quantidade Vendida")
            path_q = "output/hist_quantidade.png"
            plt.tight_layout()
            plt.savefig(path_q)
            plt.close()
            print(f"Salvo: {path_q}")
        else:
            print("Coluna 'Quantity_Sold' não encontrada no DataFrame")

        # Histograma do valor de vendas
        if 'Sales_Amount' in df.columns:
            plt.figure(figsize=(8,5))
            df['Sales_Amount'].hist()
            plt.title("Distribuição do Valor de Vendas")
            path_s = "output/hist_vendas.png"
            plt.tight_layout()
            plt.savefig(path_s)
            plt.close()
            print(f"Salvo: {path_s}")
        else:
            print("Coluna 'Sales_Amount' não encontrada no DataFrame")

        # Histograma do custo unitário
        if 'Unit_Cost' in df.columns:
            plt.figure(figsize=(8,5))
            df['Unit_Cost'].hist()
            plt.title("Distribuição do Custo Unitário")
            path_uc = "output/hist_unit_cost.png"
            plt.tight_layout()
            plt.savefig(path_uc)
            plt.close()
            print(f"Salvo: {path_uc}")
        else:
            print("Coluna 'Unit_Cost' não encontrada")

        # Histograma do preço unitário
        if 'Unit_Price' in df.columns:
            plt.figure(figsize=(8,5))
            df['Unit_Price'].hist()
            plt.title("Distribuição do Preço Unitário")
            path_up = "output/hist_unit_price.png"
            plt.tight_layout()
            plt.savefig(path_up)
            plt.close()
            print(f"Salvo: {path_up}")
        else:
            print("Coluna 'Unit_Price' não encontrada")
    except Exception as e:
        print(f"Erro em gerar_histogramas: {e}")
        raise