# ========================================
# ARQUIVO DE PIZZA - pizza.py
# ========================================
# Esse arquivo monta os gráficos de pizza

import matplotlib
matplotlib.use('Agg')  # Para salvar sem abrir janela
import matplotlib.pyplot as plt
import os

def gerar_pizza(df):
    """
    Gera 3 gráficos de pizza com os dados da base.
    """
    try:
        print("Gerando gráficos de pizza...")
        os.makedirs('output', exist_ok=True)

        # Pizza por região
        if 'Region' in df.columns:
            df['Region'].value_counts().plot.pie(autopct='%1.1f%%')
            plt.title("Distribuição por Região")
            path_r = "output/pizza_regiao.png"
            plt.savefig(path_r)
            plt.close()
            print(f"Salvo: {path_r}")
        else:
            print("Coluna 'Region' não encontrada")

        # Pizza por categoria do produto
        if 'Product_Category' in df.columns:
            df['Product_Category'].value_counts().plot.pie(autopct='%1.1f%%')
            plt.title("Distribuição por Categoria")
            path_c = "output/pizza_categoria.png"
            plt.savefig(path_c)
            plt.close()
            print(f"Salvo: {path_c}")
        else:
            print("Coluna 'Product_Category' não encontrada")

        # Pizza por tipo de cliente
        if 'Customer_Type' in df.columns:
            df['Customer_Type'].value_counts().plot.pie(autopct='%1.1f%%')
            plt.title("Tipo de Cliente")
            path_t = "output/pizza_cliente.png"
            plt.savefig(path_t)
            plt.close()
            print(f"Salvo: {path_t}")
        else:
            print("Coluna 'Customer_Type' não encontrada")
    except Exception as e:
        print(f"Erro em gerar_pizza: {e}")
        raise