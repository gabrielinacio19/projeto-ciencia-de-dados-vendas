# ========================================
# ARQUIVO DE BARRAS - barra.py
# ========================================
# Esse arquivo monta os gráficos de barras

import matplotlib
matplotlib.use('Agg')  # Para salvar sem abrir janela
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter  # Para formatar o eixo
import os

def _annotar_barras(ax):
    """
    Coloca os valores em cima das barras.
    """
    for container in ax.containers:
        ax.bar_label(container, fmt='%.0f', padding=3)

def _formatar_moeda_br(valor):
    """
    Converte o valor para um formato parecido com moeda.
    """
    return f"R$ {valor:,.0f}".replace(',', '.')

def _formatar_moeda_axis(valor, posicao):
    """
    Ajuda a mostrar o valor do eixo Y formatado.
    """
    return _formatar_moeda_br(valor)

def gerar_barra(df):
    """
    Gera 3 gráficos de barras com a base.
    """
    try:
        print("Gerando gráficos de barra...")
        os.makedirs('output', exist_ok=True)

        # Barras por categoria
        if 'Product_Category' in df.columns:
            ax = df['Product_Category'].value_counts().plot.bar(figsize=(8, 5))
            plt.title("Produtos por Categoria")
            _annotar_barras(ax)
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            path_c = "output/barra_categoria.png"
            plt.savefig(path_c)
            plt.close()
            print(f"Salvo: {path_c}")
        else:
            print("Coluna 'Product_Category' não encontrada")

        # Barras por região
        if 'Region' in df.columns and 'Sales_Amount' in df.columns:
            ax = df.groupby('Region')['Sales_Amount'].sum().plot.bar(figsize=(8, 5))
            plt.title("Vendas por Região")
            ax.ticklabel_format(axis='y', style='plain', useOffset=False)
            ax.yaxis.set_major_formatter(FuncFormatter(_formatar_moeda_axis))
            ax.set_ylabel("Valor de Vendas")
            for container in ax.containers:
                labels = [_formatar_moeda_br(valor) for valor in container.datavalues]
                ax.bar_label(container, labels=labels, padding=3)
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            path_r = "output/barra_regiao.png"
            plt.savefig(path_r)
            plt.close()
            print(f"Salvo: {path_r}")
        else:
            print("Colunas 'Region' e/ou 'Sales_Amount' não encontradas")

        # Barras por vendedor
        if 'Sales_Rep' in df.columns:
            ax = df['Sales_Rep'].value_counts().plot.bar(figsize=(8, 5))
            plt.title("Vendas por Vendedor")
            _annotar_barras(ax)
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            path_sr = "output/barra_sales_rep.png"
            plt.savefig(path_sr)
            plt.close()
            print(f"Salvo: {path_sr}")
        else:
            print("Coluna 'Sales_Rep' não encontrada")
    except Exception as e:
        print(f"Erro em gerar_barra: {e}")
        raise