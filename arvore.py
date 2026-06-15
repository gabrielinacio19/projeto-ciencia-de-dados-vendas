# ========================================
# ÁRVORE DE DECISÃO
# ========================================
# Este módulo classifica se uma venda é alta ou baixa com base na mediana.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

from ml_utils import garantir_output, carregar_base, preparar_dados_ml


def executar_arvore_decisao():
    """Treina a árvore de decisão, mede a acurácia e salva a visualização da árvore."""
    garantir_output()
    df = preparar_dados_ml(carregar_base())

    # Define a variável alvo: 1 = alta venda, 0 = baixa venda.
    X = df[["Quantity_Sold", "Unit_Cost", "Unit_Price"]]
    y = df["Alta_Venda"]

    # Separa dados de treino e teste.
    X_treino, X_teste, y_treino, y_teste = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Treina a árvore de decisão.
    modelo = DecisionTreeClassifier(max_depth=4, random_state=42)
    modelo.fit(X_treino, y_treino)

    previsoes = modelo.predict(X_teste)
    acuracia = accuracy_score(y_teste, previsoes)

    print("\n===== ÁRVORE DE DECISÃO =====")
    print(f"Acurácia: {acuracia:.4f}")
    print(classification_report(y_teste, previsoes, target_names=["Venda Baixa", "Venda Alta"]))

    # Desenha a árvore para facilitar a leitura visual.
    nomes_variaveis = [
        "Quantidade Vendida",
        "Custo Unitário",
        "Preço Unitário",
    ]
    plt.figure(figsize=(18, 8))
    plot_tree(
        modelo,
        feature_names=nomes_variaveis,
        class_names=["Venda Baixa", "Venda Alta"],
        filled=True,
        rounded=True,
        fontsize=8,
    )
    plt.title("Árvore de Decisão - Venda Alta ou Baixa")
    plt.tight_layout()
    plt.savefig("output/arvore_decisao.png", dpi=150)
    plt.close()
    print("Salvo: output/arvore_decisao.png")

    return modelo, acuracia
