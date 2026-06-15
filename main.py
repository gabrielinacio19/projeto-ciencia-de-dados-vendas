# ========================================
# ARQUIVO PRINCIPAL - main.py
# ========================================
# Esse é o arquivo que roda tudo do projeto

import os
from dados import carregar_dados
from histogramas import gerar_histogramas
from estatisticas import calcular_estatisticas
from dispersao import gerar_dispersao
from pizza import gerar_pizza
from barra import gerar_barra
from regressao import executar_regressao_linear
from regressao_logistica import executar_regressao_logistica
from arvore import executar_arvore_decisao
from random_forest import executar_random_forest
from kmeans import executar_kmeans
from prescritiva import gerar_recomendacoes

# Cria a pasta onde os gráficos vão ser salvos
os.makedirs("output", exist_ok=True)

# Carrega os dados da base
df = carregar_dados()

# Roda todas as análises e gera os gráficos
gerar_histogramas(df)      # Histogramas
calcular_estatisticas(df)  # Estatísticas básicas
gerar_dispersao(df)        # Gráfico de dispersão
gerar_pizza(df)            # Gráficos de pizza
gerar_barra(df)            # Gráficos de barras

# Novas etapas de análise preditiva e prescritiva
executar_regressao_linear()
executar_regressao_logistica()
executar_arvore_decisao()
executar_random_forest()
executar_kmeans()
gerar_recomendacoes()
