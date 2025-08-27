import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------------
# CONFIGURAÇÃO DA PÁGINA
# ------------------------------
st.set_page_config(page_title="Exploração por Gênero e País", layout="wide")

# ------------------------------
# CARREGAR OS DADOS
# ------------------------------
@st.cache_data
def load_data():
    df = pd.read_parquet("netflix_clean.parquet")
    return df

df = load_data()

# ------------------------------
# LISTA DE GÊNEROS E PAÍSES
# ------------------------------
genero_cols = df.columns[10:52].tolist()
paises_cols = df.columns[52:173].tolist()  # colunas booleanas de países

# ------------------------------
# CONFIGURAR FILTROS NA SIDEBAR
# ------------------------------
st.sidebar.title("Filtros")

# Filtro por gêneros
generos = st.sidebar.multiselect(
    "Selecione os Gêneros",
    options=genero_cols,
    default=[]
)

# Filtro por países - usando as colunas booleanas
paises = st.sidebar.multiselect(
    "Selecione os Países",
    options=paises_cols,
    default=[]
)

# Filtro por ano
anos = st.sidebar.slider(
    "Selecione o intervalo de anos",
    int(df['Year'].min()),
    int(df['Year'].max()),
    (int(df['Year'].min()), int(df['Year'].max()))
)

# ------------------------------
# APLICAR FILTROS
# ------------------------------
df_filtrado = df.copy()

if generos:
    df_filtrado = df_filtrado[df_filtrado[generos].any(axis=1)]

if paises:
    df_filtrado = df_filtrado[df_filtrado[paises].any(axis=1)]

df_filtrado = df_filtrado[(df_filtrado['Year'] >= anos[0]) & (df_filtrado['Year'] <= anos[1])]

# ------------------------------
# MÉTRICAS GERAIS
# ------------------------------
st.subheader("📌 Métricas Principais")

total_filmes = df_filtrado[df_filtrado["Category"] == "Movie"].shape[0]
total_series = df_filtrado[df_filtrado["Category"] == "TV Show"].shape[0]
media_duracao_filmes = df_filtrado[df_filtrado["Category"] == "Movie"]["Duration_Minutes"].mean()
media_temporadas_series = df_filtrado[df_filtrado["Category"] == "TV Show"]["Duration_Seasons"].mean()

col1, col2 = st.columns(2)
with col1:
    st.metric("🎬 Total de Filmes", total_filmes)
    st.metric("⏱️ Média Duração Filmes (min)", f"{media_duracao_filmes:.1f}" if not pd.isna(media_duracao_filmes) else "-")
with col2:
    st.metric("📺 Total de Séries", total_series)
    st.metric("📊 Média Temporadas Séries", f"{media_temporadas_series:.1f}" if not pd.isna(media_temporadas_series) else "-")

# ------------------------------
# GRÁFICO 1: DISTRIBUIÇÃO DE GÊNEROS
# ------------------------------
st.subheader("Distribuição de Gêneros")
if generos:
    generos_count = df_filtrado[generos].sum().sort_values(ascending=True)
else:
    generos_count = df_filtrado[genero_cols].sum().sort_values(ascending=True)

fig1 = px.bar(
    generos_count,
    x=generos_count.values,
    y=generos_count.index,
    orientation="h",
    title="Quantidade de Títulos por Gênero",
    labels={"x": "Quantidade", "y": "Gênero"}
)
st.plotly_chart(fig1, use_container_width=True)

# ------------------------------
# GRÁFICO 2: DISTRIBUIÇÃO POR PAÍS
# ------------------------------
st.subheader("Distribuição por País")

# Contagem de países com base nas colunas booleanas
paises_count = df_filtrado[paises_cols].sum().sort_values(ascending=True).tail(15)

fig2 = px.bar(
    x=paises_count.values,
    y=paises_count.index,
    orientation="h",
    title="Top 15 Países com Mais Títulos",
    labels={"x": "Quantidade", "y": "País"}
)
st.plotly_chart(fig2, use_container_width=True)

# ------------------------------
# GRÁFICO 3: MATRIZ GÊNERO x PAÍS
# ------------------------------
st.subheader("Matriz Gênero x País")
matriz = df_filtrado.groupby(df_filtrado.index)[genero_cols + paises_cols].sum()
matriz = df_filtrado[paises_cols + genero_cols].groupby(df_filtrado.index).sum()

fig3 = px.imshow(
    df_filtrado[paises_cols].T.dot(df_filtrado[genero_cols]),
    aspect="auto",
    title="Quantidade de Títulos por Gênero e País",
    labels=dict(x="Gênero", y="País", color="Qtd. Títulos")
)
st.plotly_chart(fig3, use_container_width=True)

# ------------------------------
# TABELA FINAL FILTRADA
# ------------------------------
st.subheader("Tabela de Títulos Filtrados")
st.dataframe(
    df_filtrado[['Title', 'Type', 'Year', 'Rating', 'Duration']],
    use_container_width=True
)
