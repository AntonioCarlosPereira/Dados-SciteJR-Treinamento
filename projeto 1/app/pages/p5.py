import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA
import warnings

# Ignora avisos para uma saída mais limpa
warnings.filterwarnings('ignore')

# Título do aplicativo
st.title("🗺️ Análise de Preferências de Gênero por País")
st.markdown("Use o painel lateral para explorar a clusterização de países com base em seus gostos por filmes e séries.")
st.divider()

# --- Funções de Preparação de Dados e Análise ---
@st.cache_data
def load_and_prepare_data():
    """Carrega o arquivo Parquet com os resultados da clusterização."""
    try:
        df_proportions = pd.read_parquet('country_clusters_results.parquet')
    except FileNotFoundError:
        st.error("Erro: O arquivo 'country_clusters_results.parquet' não foi encontrado. Por favor, rode a análise de clusterização e exporte o arquivo antes de usar esta aplicação.")
        st.stop()
    
    return df_proportions

def get_pca_data(df):
    """Aplica PCA e retorna o DataFrame com componentes e loadings."""
    # Defina as colunas de gêneros (excluindo a coluna 'cluster')
    genre_columns = [col for col in df.columns if col != 'cluster']
    
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(df[genre_columns])
    
    df_pca = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'], index=df.index)
    
    # Análise para nomear os eixos
    pc1_loadings = pd.Series(pca.components_[0], index=genre_columns)
    pc2_loadings = pd.Series(pca.components_[1], index=genre_columns)
    
    xlabel = f"Componente Principal 1 (Tendência: {pc1_loadings.idxmax()} vs. {pc1_loadings.idxmin()})"
    ylabel = f"Componente Principal 2 (Tendência: {pc2_loadings.idxmax()} vs. {pc2_loadings.idxmin()})"
    
    return df_pca, xlabel, ylabel

# --- Layout da Barra Lateral (Controles Interativos) ---
with st.sidebar:
    st.header("Opções de Visualização")
    show_labels = st.checkbox("Exibir Nomes dos Países", value=False)
    st.divider()
    st.info("Passe o mouse sobre os pontos para ver os detalhes de cada país e seu cluster.")

# --- Execução Principal da Aplicação ---
df_proportions = load_and_prepare_data()

# Aplica o PCA para visualização
df_pca, xlabel, ylabel = get_pca_data(df_proportions.drop('cluster', axis=1))
df_pca['cluster'] = df_proportions['cluster']

# Mapeia os clusters para strings para a legenda
df_pca['cluster_name'] = df_pca['cluster'].astype(str)

# Cria o gráfico de dispersão interativo com Plotly Express
fig = px.scatter(
    df_pca,
    x='PC1',
    y='PC2',
    color='cluster_name',
    hover_data={'PC1': False, 'PC2': False, 'cluster_name': False},
    custom_data=[df_pca.index],
    labels={'PC1': xlabel, 'PC2': ylabel, 'cluster_name': 'Cluster'},
    title=f'Clusters de Países'
)

# Adiciona o nome do país como anotação se a caixa de seleção estiver marcada
if show_labels:
    for i, row in df_pca.iterrows():
        fig.add_annotation(
            x=row['PC1'],
            y=row['PC2'],
            text=i,
            showarrow=False,
            font=dict(size=10, color="white"),
            yanchor="bottom",
            yshift=5
        )

# Exibe o gráfico no aplicativo
st.plotly_chart(fig, use_container_width=True)

# --- Exibe a lista de países por cluster ---
st.header("Países por Cluster")
cluster_dict = {}
for cluster_id in sorted(df_pca['cluster'].unique()):
    countries = df_pca[df_pca['cluster'] == cluster_id].index.tolist()
    cluster_dict[f"Cluster {cluster_id}"] = countries

st.json(cluster_dict)
