import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Análise de Dados Globais",
    page_icon="🌍",
    layout="centered"
)

# Título principal
st.title("🌍 Dashboard de Análise Global Netflix")

# Subtítulo
st.subheader("Visualize dados por país, gênero e Ano")

# Breve descrição
st.markdown("""
Bem-vindo ao **Dashboard de Análise Global**!  
Aqui você pode:
- 📊 Explorar gráficos interativos
- 🎭 Filtrar informações por **país** e **gênero**

Navegue pelas páginas no menu lateral para começar!
""")

# Uma imagem ilustrativa
st.image(
    "https://files.tecnoblog.net/wp-content/uploads/2022/08/capa-netflix-3_thumb_tb-1060x596.png",
    caption="Exploração de dados pelo mundo",
    use_container_width=True
)

# Separador
st.markdown("---")


# Rodapé
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "© 2025 - Projeto de Visualização Global"
    "</div>",
    unsafe_allow_html=True
)
