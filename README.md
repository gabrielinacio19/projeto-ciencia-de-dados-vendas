# 📊 Previsão de Ruptura de Estoques de Vendas

## 📌 Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de aplicar técnicas de Ciência de Dados em uma base de vendas, utilizando análises descritivas, diagnósticas, preditivas e prescritivas para apoiar a tomada de decisão.

A partir dos dados históricos de vendas, foram identificados padrões, realizadas previsões e geradas recomendações estratégicas que podem auxiliar empresas na compreensão de seu desempenho e no planejamento de ações futuras.

---

## 🎯 Objetivos

* Compreender o comportamento das vendas por meio de análises exploratórias;
* Identificar padrões e relações entre variáveis;
* Aplicar modelos de Machine Learning para previsão e classificação;
* Gerar recomendações para apoio à tomada de decisão;
* Demonstrar a aplicação prática de técnicas de Ciência de Dados.

---

## 📂 Estrutura do Projeto

```text
projeto-ciencia-de-dados-vendas/
│
├── data/
│   └── sales_data.csv
│
├── output/
│   └── gráficos gerados pelo sistema
│
├── main.py
├── dados.py
├── estatisticas.py
├── histogramas.py
├── dispersao.py
├── pizza.py
├── barra.py
│
├── regressao.py
├── regressao_logistica.py
├── arvore.py
├── random_forest.py
├── kmeans.py
├── prescritiva.py
├── ml_utils.py
│
└── README.md
```

---

## 📊 Análises Realizadas

### Análise Descritiva

Utilizada para resumir e compreender os dados da base por meio de:

* Histogramas;
* Gráficos de barras;
* Gráficos de pizza;
* Estatísticas descritivas.

### Análise Diagnóstica

Responsável por identificar relações entre variáveis através de:

* Gráficos de dispersão;
* Exploração de padrões presentes nos dados.

### Análise Preditiva

Aplicação de modelos de Machine Learning para previsão e classificação:

#### Regressão Linear

Prevê o valor das vendas com base em variáveis numéricas da base.

#### Regressão Logística

Classifica registros em vendas altas ou baixas.

#### Árvore de Decisão

Cria regras para classificação dos dados de forma interpretável.

#### Random Forest

Utiliza múltiplas árvores de decisão para melhorar a precisão das classificações.

#### K-Means

Agrupa registros semelhantes em diferentes clusters.

### Análise Prescritiva

Gera recomendações estratégicas com base nos resultados encontrados pelos modelos preditivos.

Exemplos:

* Priorização de regiões com maior potencial de receita;
* Investimento em categorias mais lucrativas;
* Estratégias de fidelização de clientes;
* Apoio à tomada de decisão baseada em dados.

---

## 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## ▶️ Como Executar

### 1. Clonar o repositório 

```bash
git clone https://github.com/gabrielinacio19/projeto-ciencia-de-dados-vendas.git
```

### 2. Instalar as dependências 

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 3. Executar o projeto

```bash
python main.py
```

Os gráficos e resultados serão gerados automaticamente na pasta `output`.

---

## 📈 Resultados

O projeto permitiu:

* Identificar padrões de comportamento das vendas;
* Aplicar técnicas de previsão e classificação;
* Agrupar perfis semelhantes de vendas;
* Gerar recomendações estratégicas baseadas em dados;
* Demonstrar a utilização prática de Ciência de Dados em um cenário empresarial.

---

## 👨‍💻 Autores

Fabricio Lucas,
Gabriel Coatti e
Gabriel Inácio

Projeto desenvolvido para fins acadêmicos na disciplina de Ciência de Dados.
