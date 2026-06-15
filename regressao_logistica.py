# ========================================
# REGRESSÃO LOGÍSTICA
# ========================================
# Este módulo classifica se uma venda é alta ou baixa usando um modelo interpretável.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import seaborn as sns

from ml_utils import garantir_output, carregar_base, preparar_dados_ml


def executar_regressao_logistica():
    """Treina a regressão logística, calcula métricas e salva a matriz de confusão."""
    garantir_output()
    df = preparar_dados_ml(carregar_base())

    # Usa a mesma base de classificação da árvore e do Random Forest.
    X = df[["Quantity_Sold", "Unit_Cost", "Unit_Price"]]
    y = df["Alta_Venda"]

    # Divide os dados mantendo o equilíbrio entre as classes.
    X_treino, X_teste, y_treino, y_teste = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Treina o modelo de regressão logística.
    modelo = LogisticRegression(max_iter=1000, random_state=42)
    modelo.fit(X_treino, y_treino)

    previsoes = modelo.predict(X_teste)
    acuracia = accuracy_score(y_teste, previsoes)
    matriz = confusion_matrix(y_teste, previsoes)

    print("\n===== REGRESSÃO LOGÍSTICA =====")
    print(f"Acurácia: {acuracia:.4f}")
    print(classification_report(y_teste, previsoes, target_names=["Venda Baixa", "Venda Alta"]))

    # Salva a matriz de confusão para leitura visual.
    plt.figure(figsize=(6, 5))
    sns.heatmap(
        matriz,
        annot=True,
        fmt="d",
        cmap="Oranges",
        cbar=False,
        xticklabels=["Baixa", "Alta"],
        yticklabels=["Baixa", "Alta"],
    )
    plt.title("Regressão Logística - Matriz de Confusão")
    plt.xlabel("Previsto")
    plt.ylabel("Real")
    plt.tight_layout()
    plt.savefig("output/regressao_logistica_confusao.png", dpi=150)
    plt.close()
    print("Salvo: output/regressao_logistica_confusao.png")

    return modelo, acuracia, matriz
