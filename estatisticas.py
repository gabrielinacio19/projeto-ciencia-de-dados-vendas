# ========================================
# ARQUIVO DE ESTATÍSTICAS - estatisticas.py
# ========================================
# Esse arquivo mostra números básicos da base

def calcular_estatisticas(df):
    """
    Mostra média, mediana e desvio padrão.
    """
    print("\n===== ESTATÍSTICAS DESCRITIVAS =====")
    
    # Estatísticas da quantidade vendida
    print("\nQuantidade Vendida:")
    print("  Média:", df['Quantity_Sold'].mean())
    print("  Mediana:", df['Quantity_Sold'].median())
    print("  Desvio Padrão:", df['Quantity_Sold'].std())

    # Estatísticas do valor de vendas
    print("\nValor de Vendas:")
    print("  Média:", df['Sales_Amount'].mean())
    print("  Mediana:", df['Sales_Amount'].median())
    print("  Desvio Padrão:", df['Sales_Amount'].std())