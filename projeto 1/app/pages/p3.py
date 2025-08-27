import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================
# CONFIGURAÇÕES DA PÁGINA
# ==========================
st.set_page_config(page_title="Análise de Diretores", layout="wide")

# ==========================
# CARREGAR OS DADOS
# ==========================
@st.cache_data
def load_data():
    df = pd.read_parquet("netflix_clean.parquet")
    return df

df = load_data()

# ==========================
# LISTAS DE COLUNAS BOOLEANAS
# ==========================
genero_cols = df.columns[10:52].tolist()   # colunas booleanas de gêneros
paises_cols = df.columns[52:173].tolist()  # colunas booleanas de países

# ==========================
# FILTROS NA SIDEBAR
# ==========================
st.sidebar.header("Filtros")

# Intervalo de anos
ano_min = int(df["Year"].min())
ano_max = int(df["Year"].max())
anos = st.sidebar.slider(
    "Selecione o intervalo de anos:",
    min_value=ano_min,
    max_value=ano_max,
    value=(ano_min, ano_max)
)

# Filtro por gêneros
generos = st.sidebar.multiselect(
    "Filtrar por gêneros:",
    options=genero_cols,
    default=[]
)

# Filtro por países usando colunas booleanas
paises = st.sidebar.multiselect(
    "Filtrar por países:",
    options=paises_cols,
    default=[]
)

# ==========================
# APLICANDO OS FILTROS
# ==========================
df_filtrado = df.copy()

# Remove diretores desconhecidos
df_filtrado = df_filtrado[df_filtrado["Director"].str.lower() != "unknown"]

# Filtro por intervalo de anos
df_filtrado = df_filtrado[
    (df_filtrado["Year"] >= anos[0]) &
    (df_filtrado["Year"] <= anos[1])
]

# Filtro por gêneros selecionados
if generos:
    df_filtrado = df_filtrado[df_filtrado[generos].any(axis=1)]

# Filtro por países selecionados
if paises:
    df_filtrado = df_filtrado[df_filtrado[paises].any(axis=1)]

# ==========================
# MÉTRICAS (KPIs)
# ==========================
st.subheader("📌 Métricas Principais")
col1, col2, col3 = st.columns(3)
col1.metric("🎬 Total de Diretores", df_filtrado["Director"].nunique())
col2.metric("📺 Total de Títulos", df_filtrado.shape[0])
col3.metric("🎞️ Total de Filmes", df_filtrado[df_filtrado["Category"] == "Movie"].shape[0])

st.markdown("---")

# ==========================
# GRÁFICO 1: TOP 10 DIRETORES
# ==========================
top_diretores = (
    df_filtrado["Director"]
    .value_counts()
    .head(10)
    .reset_index()
)
top_diretores.columns = ["Director", "Total"]

fig_top_diretores = px.bar(
    top_diretores,
    x="Total",
    y="Director",
    orientation="h",
    title="🎥 Top 10 Diretores com Mais Títulos",
    labels={"Total": "Quantidade de Títulos", "Director": "Diretor"}
)
st.plotly_chart(fig_top_diretores, use_container_width=True)

# ==========================
# GRÁFICO 2: DISTRIBUIÇÃO DE TÍTULOS POR ANO
# ==========================
fig_box_ano = px.box(
    df_filtrado,
    x="Year",
    title="Distribuição de Títulos por Ano"
)
st.plotly_chart(fig_box_ano, use_container_width=True)

# ==========================
# GRÁFICO 3: DISTRIBUIÇÃO DE DURAÇÃO
# ==========================
if "Duration" in df_filtrado.columns:
    fig_duration = px.histogram(
        df_filtrado,
        x="Duration",
        nbins=30,
        title="Distribuição da Duração dos Títulos"
    )
    st.plotly_chart(fig_duration, use_container_width=True)

# ==========================
# GRÁFICO 4: DISTRIBUIÇÃO DE DIRETORES POR GÊNEROS
# ==========================
st.subheader("🎭 Distribuição de Diretores por Gêneros")
if generos:
    genero_diretores = df_filtrado[generos].sum().sort_values(ascending=True)
else:
    genero_diretores = df_filtrado[genero_cols].sum().sort_values(ascending=True)

fig_genero_diretores = px.bar(
    genero_diretores,
    x=genero_diretores.values,
    y=genero_diretores.index,
    orientation="h",
    title="Diretores por Gênero",
    labels={"x": "Quantidade de Títulos", "y": "Gênero"}
)
st.plotly_chart(fig_genero_diretores, use_container_width=True)

# ==========================
# TABELA FINAL
# ==========================
st.subheader("📄 Tabela de Títulos Filtrados")
st.dataframe(df_filtrado)
