# ========================================
# RANDOM FOREST
# ========================================
# Este módulo melhora a classificação de vendas altas/baixas e mostra a importância das variáveis.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

from ml_utils import garantir_output, carregar_base, preparar_dados_ml


def executar_random_forest():
    """Treina o Random Forest, calcula métricas e salva matriz de confusão e importâncias."""
    garantir_output()
    df = preparar_dados_ml(carregar_base())

    # Usa as mesmas variáveis da árvore para comparação justa.
    X = df[["Quantity_Sold", "Unit_Cost", "Unit_Price"]]
    y = df["Alta_Venda"]

    X_treino, X_teste, y_treino, y_teste = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Treina o ensemble de árvores.
    modelo = RandomForestClassifier(n_estimators=200, random_state=42)
    modelo.fit(X_treino, y_treino)

    previsoes = modelo.predict(X_teste)
    acuracia = accuracy_score(y_teste, previsoes)
    matriz = confusion_matrix(y_teste, previsoes)

    print("\n===== RANDOM FOREST =====")
    print(f"Acurácia: {acuracia:.4f}")
    print(classification_report(y_teste, previsoes, target_names=["Baixa Venda", "Alta Venda"]))

    # Salva a matriz de confusão como mapa de calor.
    plt.figure(figsize=(6, 5))
    sns.heatmap(matriz, annot=True, fmt="d", cmap="Blues", cbar=False, vmin=0, vmax=100,
                xticklabels=["Baixa", "Alta"], yticklabels=["Baixa", "Alta"])
    plt.title("Random Forest - Matriz de Confusão")
    plt.xlabel("Previsto")
    plt.ylabel("Real")
    plt.tight_layout()
    plt.savefig("output/random_forest_confusao.png", dpi=150)
    plt.close()
    print("Salvo: output/random_forest_confusao.png")

    # Salva a importância das variáveis.
    importancias = modelo.feature_importances_
    plt.figure(figsize=(7, 5))
    plt.barh(list(X.columns), importancias, color="#2a6fdb")
    plt.title("Random Forest - Importância das Variáveis")
    plt.xlabel("Importância")
    plt.ylabel("Variável")
    plt.tight_layout()
    plt.savefig("output/random_forest_importancia.png", dpi=150)
    plt.close()
    print("Salvo: output/random_forest_importancia.png")

    return modelo, acuracia, matriz, importancias
