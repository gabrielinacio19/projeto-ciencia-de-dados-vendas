# ========================================
# MODELO DE REGRESSÃO LINEAR
# ========================================
# Este módulo prevê o valor total de vendas usando quantidade, custo e preço.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

from ml_utils import garantir_output, carregar_base, preparar_dados_ml


def executar_regressao_linear():
    """Treina a regressão linear, calcula métricas e salva o gráfico de previsão."""
    garantir_output()
    df = preparar_dados_ml(carregar_base())

    # Seleciona as variáveis que explicam o valor total de vendas.
    X = df[["Quantity_Sold", "Unit_Cost", "Unit_Price"]]
    y = df["Sales_Value"]

    # Divide os dados entre treino e teste para avaliar o modelo de forma justa.
    X_treino, X_teste, y_treino, y_teste = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Treina a regressão linear.
    modelo = LinearRegression()
    modelo.fit(X_treino, y_treino)

    # Gera previsões no conjunto de teste.
    previsoes = modelo.predict(X_teste)

    # Calcula métricas de desempenho.
    mae = mean_absolute_error(y_teste, previsoes)
    mse = mean_squared_error(y_teste, previsoes)
    rmse = mse ** 0.5
    r2 = r2_score(y_teste, previsoes)

    print("\n===== REGRESSÃO LINEAR =====")
    print("Coeficientes:")
    for nome, coef in zip(X.columns, modelo.coef_):
        print(f"  {nome}: {coef:.4f}")
    print(f"Intercepto: {modelo.intercept_:.4f}")
    print(f"MAE: {mae:.4f}")
    print(f"MSE: {mse:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"R²: {r2:.4f}")

    # Cria o gráfico comparando valores reais e previstos.
    plt.figure(figsize=(8, 5))
    plt.scatter(y_teste, previsoes, alpha=0.7, color="#2a6fdb")
    limite_min = min(y_teste.min(), previsoes.min())
    limite_max = max(y_teste.max(), previsoes.max())
    plt.plot([limite_min, limite_max], [limite_min, limite_max], "r--", linewidth=2)
    plt.title("Regressão Linear - Valor Real x Valor Previsto")
    plt.xlabel("Valor de vendas real")
    plt.ylabel("Valor de vendas previsto")
    plt.tight_layout()
    plt.savefig("output/regressao_linear.png", dpi=150)
    plt.close()
    print("Salvo: output/regressao_linear.png")

    return modelo, {"MAE": mae, "MSE": mse, "RMSE": rmse, "R2": r2}
