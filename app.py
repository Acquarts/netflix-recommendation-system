import streamlit as st
import pandas as pd
import os
from recommendation_system import NetflixRecommendationSystem

# Configuración de la página
st.set_page_config(
    page_title="🎬 Netflix Recommendation System",
    page_icon="🍿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .title-main {
        color: #E50914;
        font-size: 3em;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .recommendation-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.8rem;
        margin: 1rem 0;
        border-left: 4px solid #E50914;
    }
    .metric-card {
        background-color: #262730;
        padding: 1.5rem;
        border-radius: 0.8rem;
        text-align: center;
        color: #E50914;
    }
    </style>
""", unsafe_allow_html=True)

# Cargar el modelo (con cache)
@st.cache_resource
def load_recommendation_system():
    """Cargar el sistema de recomendación"""
    csv_path = 'netflix_titles.csv'
    
    # Si no existe el CSV, copiarlo del directorio de uploads
    if not os.path.exists(csv_path):
        import shutil
        shutil.copy('/mnt/user-data/uploads/netflix_titles.csv', csv_path)
    
    return NetflixRecommendationSystem(csv_path)

# Inicializar el sistema
with st.spinner('🔄 Cargando el sistema de recomendación...'):
    recommender = load_recommendation_system()

# Header
st.markdown('<div class="title-main">🎬 Netflix Recommendation System</div>', unsafe_allow_html=True)
st.markdown("**Descubre nuevas películas y series basadas en tus preferencias**", unsafe_allow_html=True)
st.divider()

# Sidebar
with st.sidebar:
    st.header("📊 Dashboard")
    
    # Obtener estadísticas
    stats = recommender.get_stats()
    
    # Mostrar métricas
    col1, col2 = st.columns(2)
    with col1:
        st.metric("📺 Total de Títulos", stats['total_titles'])
        st.metric("🎥 Películas", stats['movies'])
    with col2:
        st.metric("📺 Series", stats['tv_shows'])
        st.metric("🎭 Géneros", stats['total_genres'])
    
    st.markdown("---")
    st.markdown("**Información del Dataset**")
    st.info(f"📅 Años: {stats['min_release_year']} - {stats['max_release_year']}")

# Tabs principales
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["🎯 Recomendaciones", "🔍 Buscar", "🎭 Géneros", "📈 Trending", "ℹ️ Información"]
)

# TAB 1: Recomendaciones
with tab1:
    st.header("🎯 Obtener Recomendaciones")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        title_input = st.text_input(
            "Ingresa el nombre de una película o serie:",
            placeholder="Ej: Breaking Bad, Inception, The Crown..."
        )
    
    with col2:
        n_recs = st.number_input(
            "Número de recomendaciones:",
            min_value=1,
            max_value=20,
            value=10
        )
    
    if title_input:
        # Verificar que el título existe
        idx = recommender.find_title_index(title_input)
        
        if idx is not None:
            # Mostrar el título original
            original = recommender.df.iloc[idx]
            
            st.success("✅ Título encontrado")
            
            with st.expander("📌 Detalles del título original", expanded=False):
                col1, col2 = st.columns([2, 1])
                with col1:
                    st.write(f"**Título:** {original['title']}")
                    st.write(f"**Tipo:** {original['type']}")
                    st.write(f"**Géneros:** {original['listed_in']}")
                    st.write(f"**Año:** {original['release_year']}")
                    st.write(f"**Rating:** {original['rating']}")
                with col2:
                    st.write(f"**Descripción:** {original['description']}")
            
            # Obtener recomendaciones
            with st.spinner("🔍 Buscando recomendaciones..."):
                recommendations = recommender.get_recommendations(title_input, n_recs)
            
            if recommendations is not None and len(recommendations) > 0:
                st.subheader(f"📌 Top {len(recommendations)} Recomendaciones")
                
                for idx, row in recommendations.iterrows():
                    # Barra de similitud
                    similarity_pct = row['similarity_score'] * 100
                    
                    with st.container():
                        col1, col2, col3 = st.columns([1, 3, 1])
                        
                        with col1:
                            st.metric(
                                "Similitud",
                                f"{similarity_pct:.1f}%",
                                delta=None
                            )
                        
                        with col2:
                            st.write(f"**{row['title']}**")
                            st.write(f"*{row['type']}* | {row['listed_in']}")
                            st.write(f"📝 {row['description'][:150]}...")
                        
                        with col3:
                            st.progress(row['similarity_score'])
                        
                        st.divider()
            else:
                st.warning("No se encontraron recomendaciones para este título.")
        else:
            st.error("❌ Título no encontrado. Intenta con otro nombre.")
            
            # Sugerir búsqueda similar
            st.info("💡 **Tip:** Usa la pestaña 'Buscar' para explorar títulos disponibles")

# TAB 2: Búsqueda
with tab2:
    st.header("🔍 Buscar Títulos")
    
    search_query = st.text_input(
        "Busca un título:",
        placeholder="Ej: Game of Thrones, Stranger Things..."
    )
    
    if search_query:
        with st.spinner("🔎 Buscando..."):
            results = recommender.search_titles(search_query)
        
        if len(results) > 0:
            st.success(f"Se encontraron {len(results)} resultados")
            st.dataframe(
                results,
                use_container_width=True,
                hide_index=True
            )
        else:
            st.warning("No se encontraron resultados para tu búsqueda.")

# TAB 3: Géneros
with tab3:
    st.header("🎭 Explorar por Géneros")
    
    # Lista de géneros comunes
    genres = [
        "Action", "Comedy", "Drama", "Romance", "Thriller", "Horror",
        "Sci-Fi", "Fantasy", "Adventure", "Documentary", "Crime",
        "Animation", "Kids", "Sports", "Stand-Up"
    ]
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        selected_genre = st.selectbox("Selecciona un género:", genres)
    
    with col2:
        limit = st.number_input("Mostrar títulos:", min_value=5, max_value=100, value=20)
    
    with st.spinner("📂 Cargando títulos..."):
        genre_results = recommender.filter_by_genre(selected_genre, limit)
    
    if len(genre_results) > 0:
        st.success(f"Se encontraron {len(genre_results)} títulos en '{selected_genre}'")
        st.dataframe(
            genre_results,
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info(f"No hay títulos disponibles para el género '{selected_genre}'")

# TAB 4: Trending
with tab4:
    st.header("📈 Títulos Más Recientes")
    
    col1, col2 = st.columns(2)
    
    with col1:
        limit = st.slider("¿Cuántos títulos mostrar?", min_value=10, max_value=100, value=20)
    
    with col2:
        content_type = st.selectbox("Filtrar por tipo:", ["Todos", "Movie", "TV Show"])
    
    with st.spinner("📂 Cargando..."):
        trending = recommender.get_trending(limit)
        
        if content_type != "Todos":
            trending = trending[trending['type'] == content_type]
    
    st.dataframe(
        trending,
        use_container_width=True,
        hide_index=True
    )

# TAB 5: Información
with tab5:
    st.header("ℹ️ Acerca del Sistema")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📌 ¿Cómo funciona?")
        st.write("""
        Este sistema utiliza **Machine Learning** para recomendaciones:
        
        1. **TF-IDF Vectorization**: Convierte descripciones y géneros en vectores numéricos
        2. **Cosine Similarity**: Calcula la similitud entre títulos
        3. **Content-Based Filtering**: Recomienda títulos similares al seleccionado
        
        **Características consideradas:**
        - 📝 Descripción del contenido
        - 🎭 Géneros
        - 👥 Elenco
        """)
    
    with col2:
        st.subheader("📊 Dataset")
        st.write(f"""
        **Netflix Titles Dataset**
        
        - **Total de títulos:** {stats['total_titles']:,}
        - **Películas:** {stats['movies']:,}
        - **Series:** {stats['tv_shows']:,}
        - **Géneros únicos:** {stats['total_genres']:,}
        - **Rango de años:** {stats['min_release_year']} - {stats['max_release_year']}
        """)
    
    st.divider()
    
    st.subheader("💡 Tips de Uso")
    st.markdown("""
    - 🔍 **Búsqueda**: Usa nombres exactos o parciales de títulos
    - 🎯 **Recomendaciones**: Mientras mayor sea el porcentaje de similitud, más parecido al título original
    - 🎭 **Géneros**: Explora nuevos contenido por categoría
    - 📈 **Trending**: Descubre los estrenos más recientes
    """)
    
    st.divider()
    
    st.info("""
    **Desarrollado con:**
    - 🐍 Python
    - 🎈 Streamlit
    - 🤖 Scikit-learn
    - 🐼 Pandas
    """)

# Footer
st.divider()
st.markdown("""
    <div style='text-align: center; color: #888; font-size: 0.9em;'>
    🍿 Netflix Recommendation System | Powered by Machine Learning
    </div>
""", unsafe_allow_html=True)
