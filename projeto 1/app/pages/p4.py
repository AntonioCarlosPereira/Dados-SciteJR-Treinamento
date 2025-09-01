import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. CONFIGURAÇÃO E CARREGAMENTO DOS DADOS ---
st.set_page_config(
    page_title="Previsão de Títulos por País",
    layout="wide"
)

st.title("📈 Previsão de Títulos por País e Gênero")
st.markdown("Selecione um ou mais países para visualizar a previsão do número total de títulos nos próximos 3 anos.")

# Tentar carregar o arquivo de previsões
try:
    df_previsoes = pd.read_parquet('previsoes_por_pais.parquet')
except FileNotFoundError:
    st.error("Arquivo de previsões não encontrado! Por favor, execute o script de geração das previsões primeiro.")
    st.stop()

# --- 2. CRIAÇÃO DO GRÁFICO INTERATIVO ---
# Criar uma caixa de seleção múltipla com os países únicos
paises_unicos = df_previsoes['pais'].unique()
paises_selecionados = st.multiselect(
    "Escolha os países para visualizar:",
    options=paises_unicos,
    default=paises_unicos[0] # Seleciona um país como padrão
)

if paises_selecionados:
    # Filtrar o DataFrame com base nos países selecionados
    df_filtrado = df_previsoes[df_previsoes['pais'].isin(paises_selecionados)]

    # Criar o gráfico de linhas interativo com Plotly
    fig = px.line(
        df_filtrado,
        x='ano',
        y='numero de titulos',
        color='pais',
        title="Previsão de Títulos nos Próximos Anos",
        labels={'ano': 'Ano', 'numero de titulos': 'Número Total de Títulos Previstos'}
    )
    
    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Por favor, selecione pelo menos um país para visualizar o gráfico.")