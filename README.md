# 🎬 Netflix Recommendation System

Un sistema inteligente de recomendación de películas y series de Netflix utilizando Machine Learning y Streamlit.

## 🌟 Características

- **Recomendaciones Personalizadas**: Basadas en análisis de similitud de contenido
- **Búsqueda Flexible**: Encuentra títulos por nombre
- **Filtrado por Género**: Explora contenido por categorías
- **Trending**: Descubre los estrenos más recientes
- **Interfaz Intuitiva**: Diseño moderno y responsivo

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**
- **Streamlit**: Framework web para data science
- **Scikit-learn**: Machine Learning (TF-IDF, Cosine Similarity)
- **Pandas**: Manipulación de datos
- **NumPy**: Computación numérica

## 📊 Algoritmo de Recomendación

El sistema utiliza **Content-Based Filtering** con:

1. **TF-IDF Vectorization**: Convierte texto (descripciones, géneros, elenco) en vectores numéricos
2. **Cosine Similarity**: Calcula similitud entre títulos
3. **Ranking**: Ordena recomendaciones por similitud

## 🚀 Instalación Local

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos

1. **Clona el repositorio**
```bash
git clone https://github.com/tu-usuario/netflix-recommendation-system.git
cd netflix-recommendation-system
```

2. **Crea un entorno virtual** (opcional pero recomendado)
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instala las dependencias**
```bash
pip install -r requirements.txt
```

4. **Copia el dataset**
```bash
# Asegúrate de que netflix_titles.csv esté en el mismo directorio que app.py
```

5. **Ejecuta la aplicación**
```bash
streamlit run app.py
```

La aplicación se abrirá en `http://localhost:8501`

## 📁 Estructura del Proyecto

```
netflix-recommendation-system/
├── app.py                          # Aplicación principal de Streamlit
├── recommendation_system.py        # Lógica del sistema de recomendación
├── requirements.txt                # Dependencias del proyecto
├── netflix_titles.csv              # Dataset de Netflix
├── README.md                       # Este archivo
└── .streamlit/
    └── config.toml                 # Configuración de Streamlit
```

## 🎯 Uso

### 1. Obtener Recomendaciones
- Ve a la pestaña "🎯 Recomendaciones"
- Ingresa el nombre de una película o serie
- Selecciona cuántas recomendaciones deseas
- El sistema mostrará títulos similares con puntuaciones de similitud

### 2. Buscar Títulos
- Ve a la pestaña "🔍 Buscar"
- Escribe parte del nombre del título
- Explora los resultados

### 3. Explorar por Género
- Ve a la pestaña "🎭 Géneros"
- Selecciona un género de la lista
- Ajusta la cantidad de títulos a mostrar

### 4. Ver Estrenos Recientes
- Ve a la pestaña "📈 Trending"
- Filtra por películas o series
- Descubre lo más nuevo

## 🌐 Deploy en Streamlit Cloud

### Opción 1: Streamlit Cloud (Recomendado)

1. **Prepara tu repositorio en GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Ve a [Streamlit Cloud](https://streamlit.io/cloud)**

3. **Conecta tu repositorio GitHub**
   - Inicia sesión con tu cuenta de GitHub
   - Autoriza Streamlit Cloud
   - Selecciona tu repositorio

4. **Configura la aplicación**
   - Repository: `tu-usuario/netflix-recommendation-system`
   - Branch: `main`
   - Main file path: `app.py`

5. **Deploy**
   - Haz clic en "Deploy"
   - Espera a que se complete

### Opción 2: Heroku

1. **Crea una cuenta en Heroku** y instala el CLI

2. **Crea los archivos necesarios**

`Procfile`:
```
web: streamlit run app.py --logger.level=error
```

`runtime.txt`:
```
python-3.11.0
```

3. **Deploy**
```bash
heroku login
heroku create tu-app-name
git push heroku main
```

### Opción 3: Deploy en AWS/GCP/Azure

Consulta la documentación específica de cada plataforma para desplegar aplicaciones Python.

## 📊 Dataset

El sistema utiliza el dataset de Netflix que contiene:
- **8,807 títulos** (películas y series)
- **Información**: tipo, título, director, elenco, país, año, rating, duración, géneros, descripción

**Fuente**: [Kaggle Netflix Titles Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows)

## 🔄 Pipeline de Datos

```
CSV Input
    ↓
Limpieza de Datos
    ↓
Combinación de Características
    ↓
TF-IDF Vectorization
    ↓
Cálculo de Similitud
    ↓
Recomendaciones
```

## 📈 Mejoras Futuras

- [ ] Sistema de ratings de usuarios
- [ ] Collaborative Filtering
- [ ] Análisis de sentimientos
- [ ] Recomendaciones por mood/vibe
- [ ] Integración con API de TMDB
- [ ] Dashboard de análisis
- [ ] Sistema de favoritos
- [ ] Exportar recomendaciones

## 🤝 Contribuciones

Las contribuciones son bienvenidas! Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la licencia MIT. Ver `LICENSE` para más detalles.

## 👨‍💻 Autor

Desarrollado como un proyecto de Machine Learning y Data Science.

## 📧 Contacto

Para preguntas o sugerencias, abre un issue en el repositorio.

## 🙏 Agradecimientos

- Dataset de Netflix en Kaggle
- Comunidad de Streamlit
- Documentación de Scikit-learn

---

⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub!
