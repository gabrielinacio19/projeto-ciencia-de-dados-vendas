# ========================================
# K-MEANS
# ========================================
# Este módulo agrupa vendas em perfis parecidos usando três variáveis numéricas.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from ml_utils import garantir_output, carregar_base, preparar_dados_ml


def executar_kmeans():
    """Agrupa as vendas em clusters e salva o gráfico de dispersão dos grupos."""
    garantir_output()
    df = preparar_dados_ml(carregar_base())

    # Seleciona as variáveis numéricas para clusterização.
    dados = df[["Quantity_Sold", "Unit_Price", "Sales_Value"]].copy()

    # Padroniza os dados para o K-Means não favorecer variáveis de escala maior.
    scaler = StandardScaler()
    dados_escalados = scaler.fit_transform(dados)

    # Cria os grupos com três clusters para representar perfis simples.
    modelo = KMeans(n_clusters=3, random_state=42, n_init=10)
    clusters = modelo.fit_predict(dados_escalados)
    df["Cluster"] = clusters

    print("\n===== K-MEANS =====")
    print(df["Cluster"].value_counts().sort_index())
    print("Centroides padronizados:")
    print(modelo.cluster_centers_)

    # Desenha a clusterização em 2D usando quantidade e preço.
    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data=df,
        x="Quantity_Sold",
        y="Unit_Price",
        hue="Cluster",
        palette="Set2",
        alpha=0.75,
    )
    plt.title("K-Means - Clusters de Vendas")
    plt.xlabel("Quantity Sold")
    plt.ylabel("Unit Price")
    plt.tight_layout()
    plt.savefig("output/kmeans_clusters.png", dpi=150)
    plt.close()
    print("Salvo: output/kmeans_clusters.png")

    return modelo, df
