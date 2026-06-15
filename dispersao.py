# ========================================
# ARQUIVO DE DISPERSÃO - dispersao.py
# ========================================
# Esse arquivo faz os gráficos de dispersão

import matplotlib
matplotlib.use('Agg')  # Para salvar sem abrir janela
import seaborn as sns  # Para fazer o gráfico de forma simples
import matplotlib.pyplot as plt
import os

def _salvar_dispersao(df, x_coluna, y_coluna, titulo, path_saida):
    """
    Cria e salva um gráfico de dispersão.
    """
    sns.scatterplot(x=x_coluna, y=y_coluna, data=df)
    plt.title(titulo)
    plt.tight_layout()
    plt.savefig(path_saida)
    plt.close()
    print(f"Salvo: {path_saida}")

def gerar_dispersao(df):
    """
    Gera 4 gráficos de dispersão com a base.
    """
    try:
        print("Gerando gráficos de dispersão...")
        os.makedirs('output', exist_ok=True)
        
        # Quantidade vendida x valor de vendas
        if 'Quantity_Sold' in df.columns and 'Sales_Amount' in df.columns:
            _salvar_dispersao(
                df,
                'Quantity_Sold',
                'Sales_Amount',
                'Quantidade vs Vendas',
                'output/dispersao1.png'
            )
        else:
            print("Colunas necessárias para a primeira dispersão não encontradas")

        # Custo unitário x preço unitário
        if 'Unit_Cost' in df.columns and 'Unit_Price' in df.columns:
            _salvar_dispersao(
                df,
                'Unit_Cost',
                'Unit_Price',
                'Custo Unitário vs Preço Unitário',
                'output/dispersao2.png'
            )
        else:
            print("Colunas necessárias para a segunda dispersão não encontradas")

        # Quantidade vendida x custo unitário
        if 'Quantity_Sold' in df.columns and 'Unit_Cost' in df.columns:
            _salvar_dispersao(
                df,
                'Quantity_Sold',
                'Unit_Cost',
                'Quantidade vs Custo Unitário',
                'output/dispersao3.png'
            )
        else:
            print("Colunas necessárias para a terceira dispersão não encontradas")

        # Quantidade vendida x preço unitário
        if 'Quantity_Sold' in df.columns and 'Unit_Price' in df.columns:
            _salvar_dispersao(
                df,
                'Quantity_Sold',
                'Unit_Price',
                'Quantidade vs Preço Unitário',
                'output/dispersao4.png'
            )
        else:
            print("Colunas necessárias para a quarta dispersão não encontradas")
    except Exception as e:
        print(f"Erro em gerar_dispersao: {e}")
        raise