import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ================================
# Carregar os dados
# ================================
@st.cache_data
def load_data():
    return pd.read_parquet("netflix_clean.parquet")

df = load_data()

st.title("📊 Visão Geral da Base Netflix")

# ================================
# Filtros
# ================================
ano_min, ano_max = int(df["Year"].min()), int(df["Year"].max())
paises = df["Country"].dropna().unique()
tipos = df["Category"].dropna().unique()

ano_sel = st.sidebar.slider(
    "Selecionar intervalo de anos",
    min_value=ano_min,
    max_value=ano_max,
    value=(ano_max - 10, ano_max)  # default últimos 10 anos
)
pais_sel = st.sidebar.multiselect("Filtrar por País", paises)
tipo_sel = st.sidebar.multiselect("Filtrar por Tipo", tipos, default=tipos)

df_filtrado = df.copy()
if ano_sel:
    df_filtrado = df[(df["Year"] >= ano_sel[0]) & (df["Year"] <= ano_sel[1])]
if pais_sel:
    df_filtrado = df_filtrado[df_filtrado["Country"].isin(pais_sel)]
if tipo_sel:
    df_filtrado = df_filtrado[df_filtrado["Category"].isin(tipo_sel)]

# ================================
# Métricas principais
# ================================
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

# ================================
# Gráfico 1 (original): Distribuição por Ano
# ================================
st.subheader("📈 Evolução de Títulos ao Longo do Tempo")
titulos_por_ano = df_filtrado.groupby("Year").size()

fig, ax = plt.subplots()
titulos_por_ano.plot(kind="line", ax=ax, marker="o")
ax.set_xlabel("Ano de Lançamento")
ax.set_ylabel("Número de Títulos")
st.pyplot(fig)

# ================================
# Gráfico 2 (original): Filmes vs Séries
# ================================
st.subheader("🎬 Proporção Filmes vs Séries")
tipo_count = df_filtrado["Category"].value_counts()

fig2, ax2 = plt.subplots()
ax2.pie(tipo_count, labels=tipo_count.index, autopct="%1.1f%%", startangle=90)
ax2.axis("equal")
st.pyplot(fig2)

# ================================
# Gráfico 3 (original): Top Países
# ================================
st.subheader("🌍 Top 10 Países com mais Títulos")
pais_count = df_filtrado["Country"].value_counts().head(10)

fig3, ax3 = plt.subplots()
pais_count.plot(kind="barh", ax=ax3)
ax3.set_xlabel("Número de Títulos")
ax3.set_ylabel("País")
st.pyplot(fig3)

# ================================
# Gráfico 4 (novo): Boxplot de Duração
# ================================
st.subheader("⏳ Distribuição de Duração por Tipo")

fig4, ax4 = plt.subplots()
df_filtrado.boxplot(column="Duration_Minutes", by="Category", ax=ax4)
ax4.set_title("Boxplot de Duração (minutos / temporadas)")
ax4.set_xlabel("Tipo")
ax4.set_ylabel("Duração")
plt.suptitle("")
st.pyplot(fig4)

# ================================
# Gráfico 5 (novo): Distribuição de Ratings
# ================================
st.subheader("⭐ Distribuição de Ratings")

rating_count = df_filtrado["Rating"].value_counts()

fig5, ax5 = plt.subplots()
rating_count.plot(kind="bar", ax=ax5)
ax5.set_xlabel("Rating")
ax5.set_ylabel("Número de Títulos")
st.pyplot(fig5)

# ================================
# Tabela com dados filtrados
# ================================
st.subheader("📋 Tabela de Títulos Filtrados")
st.dataframe(df_filtrado[["Title", "Category", "Year", "Country", "Rating"]].reset_index(drop=True))
