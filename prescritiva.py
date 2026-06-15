# ========================================
# SISTEMA PRESCRITIVO
# ========================================
# Este módulo gera recomendações automáticas com base nos padrões encontrados.

from collections import Counter

from ml_utils import carregar_base, preparar_dados_ml


def _formatar_top(series, n=3):
    """Formata os top n valores de uma série em texto simples."""
    return series.value_counts().head(n)


def gerar_recomendacoes():
    """Analisa a base e imprime recomendações práticas para o projeto."""
    df = preparar_dados_ml(carregar_base())

    print("\n===== SISTEMA PRESCRITIVO =====")

    # 1. Regiões com maior potencial de receita.
    receita_regiao = df.groupby("Region", as_index=False)["Sales_Value"].sum().sort_values("Sales_Value", ascending=False)
    melhor_regiao = receita_regiao.iloc[0]
    pior_regiao = receita_regiao.iloc[-1]
    print(f"1) Priorizar a região {melhor_regiao['Region']} porque ela concentra a maior receita total ({melhor_regiao['Sales_Value']:.2f}).")
    print(f"   Recomenda-se reforçar ações na região {pior_regiao['Region']}, que apresentou a menor receita ({pior_regiao['Sales_Value']:.2f}).")

    # 2. Categorias mais lucrativas.
    receita_categoria = df.groupby("Product_Category", as_index=False)["Sales_Value"].sum().sort_values("Sales_Value", ascending=False)
    top_categoria = receita_categoria.iloc[0]
    print(f"2) Investir mais em {top_categoria['Product_Category']} porque é a categoria com maior faturamento total ({top_categoria['Sales_Value']:.2f}).")

    # 3. Vendedores com melhor desempenho.
    vendas_representante = df.groupby("Sales_Rep", as_index=False)["Sales_Value"].sum().sort_values("Sales_Value", ascending=False)
    top_rep = vendas_representante.iloc[0]
    print(f"3) Identificar e replicar as práticas de {top_rep['Sales_Rep']}, que lidera em faturamento ({top_rep['Sales_Value']:.2f}).")

    # 4. Retenção de clientes.
    clientes = df["Customer_Type"].value_counts()
    proporcao_recorrentes = clientes.get("Returning", 0) / len(df)
    if proporcao_recorrentes < 0.5:
        print("4) Fortalecer retenção de clientes com programas de fidelidade e pós-venda, pois a base recorrente está abaixo de 50%.")
    else:
        print("4) Manter a estratégia de fidelização, pois a proporção de clientes recorrentes está equilibrada com a de novos clientes.")

    # 5. Segmentos prioritários para campanhas.
    ticket_segmento = df.groupby("Customer_Type", as_index=False)["Sales_Value"].mean().sort_values("Sales_Value", ascending=False)
    segmento_top = ticket_segmento.iloc[0]
    print(f"5) Direcionar campanhas para o segmento {segmento_top['Customer_Type']}, que apresenta maior valor médio de venda ({segmento_top['Sales_Value']:.2f}).")

    # Diagnóstico extra baseado em clusters, se houver.
    if "Cluster" in df.columns:
        clusters = df["Cluster"].value_counts().sort_index()
        maior_cluster = clusters.idxmax()
        print(f"6) Explorar o cluster {maior_cluster} como grupo prioritário, pois é o cluster com maior volume de registros.")

    return {
        "receita_regiao": receita_regiao,
        "receita_categoria": receita_categoria,
        "vendas_representante": vendas_representante,
    }
