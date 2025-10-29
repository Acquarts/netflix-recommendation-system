# 🚀 Inicio Rápido - Sistema de Recomendación Netflix

## 📁 Archivos Incluidos

```
📦 Netflix Recommendation System
├── 📄 app.py                      # Aplicación Streamlit
├── 📄 recommendation_system.py   # Lógica de recomendación
├── 📄 example_usage.py           # Script de ejemplo
├── 📄 requirements.txt           # Dependencias
├── 📄 netflix_titles.csv         # Dataset (8,807 títulos)
├── 📄 README.md                  # Documentación completa
├── 📄 DEPLOY.md                  # Guía de deploy
└── 📄 setup.sh                   # Script de setup
```

---

## ⚡ Instalación en 5 Minutos

### 1️⃣ Clonar o Descargar

```bash
# Si usas Git
git clone https://github.com/TU_USUARIO/netflix-recommendation-system.git
cd netflix-recommendation-system

# O simplemente descarga los archivos
```

### 2️⃣ Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 3️⃣ Ejecutar la Aplicación

```bash
streamlit run app.py
```

🎉 **¡Listo!** La app abrirá en http://localhost:8501

---

## 🎯 Uso de la Aplicación

### 🎯 Tab 1: Recomendaciones
- Escribe el nombre de una película o serie
- Ajusta cuántas recomendaciones deseas
- El sistema muestra títulos similares con % de similitud

### 🔍 Tab 2: Buscar
- Busca títulos por nombre
- Resultados en tiempo real

### 🎭 Tab 3: Géneros
- Selecciona un género (Action, Drama, Comedy, etc.)
- Explora títulos por categoría

### 📈 Tab 4: Trending
- Ve los estrenos más recientes
- Filtra por películas o series

### ℹ️ Tab 5: Información
- Estadísticas del dataset
- Cómo funciona el sistema

---

## 💡 Ejemplos de Uso

### Obtener recomendaciones:
```
Ingresa: "Breaking Bad"
Resultado: Verás títulos similares como Better Call Saul, Occupied, etc.
```

### Buscar películas:
```
Busca: "Game of Thrones"
Resultado: Encontrará todos los títulos que contienen "Game of Thrones"
```

### Explorar géneros:
```
Selecciona: "Sci-Fi"
Resultado: Todas las películas y series de Ciencia Ficción
```

---

## 🔧 Para Desarrolladores

### Probar el sistema localmente:

```bash
python example_usage.py
```

Esto mostrará:
- Estadísticas del dataset
- Búsquedas de ejemplo
- Recomendaciones
- Filtrados por género

### Personalizar el sistema:

Edita `recommendation_system.py` para:
- Cambiar parámetros de TF-IDF
- Agregar nuevas funciones
- Optimizar el cálculo de similitud

---

## 🌐 Deploy en Streamlit Cloud (Gratis)

### Opción más fácil:

1. **Sube a GitHub**
```bash
git init
git add .
git commit -m "Netflix Recommendation System"
git push origin main
```

2. **Ve a https://streamlit.io/cloud**

3. **Haz clic en "New app"**
   - Repository: `TU_USUARIO/netflix-recommendation-system`
   - Main file: `app.py`

4. **Haz clic en "Deploy"**

5. **¡Listo en 2 minutos!** Tu URL será:
```
https://share.streamlit.io/TU_USUARIO/netflix-recommendation-system
```

**[Ver guía completa de deploy →](DEPLOY.md)**

---

## 📊 Dataset

- **Total de títulos:** 8,807
- **Películas:** 6,131
- **Series:** 2,676
- **Géneros únicos:** 1,680
- **Años:** 1925 - 2021

---

## 🤖 Algoritmo

**Content-Based Filtering con TF-IDF:**

1. **TF-IDF Vectorization** → Convierte descripciones en vectores
2. **Cosine Similarity** → Calcula similitud entre títulos
3. **Ranking** → Ordena por mayor similitud

Características consideradas:
- 📝 Descripción del contenido
- 🎭 Géneros
- 👥 Elenco

---

## ❓ Preguntas Frecuentes

### ¿Por qué algunas búsquedas no encuentran resultados?
→ Intenta escribir parte del nombre (ej: "Breaking" en lugar de "Breaking Bad")

### ¿Puedo agregar mi propio dataset?
→ Sí, reemplaza `netflix_titles.csv` con otro CSV que tenga columnas similares

### ¿Cómo mejoro las recomendaciones?
→ Edita los parámetros en `recommendation_system.py`:
```python
self.tfidf = TfidfVectorizer(
    max_features=5000,      # Aumenta para más palabras
    ngram_range=(1, 2),     # Cambia para diferentes patrones
    min_df=2,               # Palabras mínimas en documentos
)
```

### ¿Funciona offline?
→ Sí, una vez cargada la aplicación no necesita internet

---

## 🐛 Troubleshooting

| Problema | Solución |
|----------|----------|
| "Module not found" | `pip install -r requirements.txt` |
| "CSV not found" | Verifica que `netflix_titles.csv` esté en la carpeta |
| "App lenta" | Es normal. El primer cálculo es pesado (~30s) |
| "Out of Memory" | Problema en Streamlit Cloud, usa Heroku |

---

## 📚 Recursos Adicionales

- 📖 [Documentación Completa](README.md)
- 🚀 [Guía de Deploy](DEPLOY.md)
- 🔗 [Documentación Streamlit](https://docs.streamlit.io)
- 📊 [Dataset en Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)

---

## 🎓 Próximos Pasos

1. ✅ Ejecuta la app localmente
2. ✅ Experimenta con recomendaciones
3. ✅ Sube a GitHub
4. ✅ Deploy en Streamlit Cloud (gratis)
5. ✅ Comparte con amigos

---

## 💬 Feedback

¿Preguntas o sugerencias?
- 📧 Crea un issue en GitHub
- 🌟 Comparte si te gustó
- 🔄 Contribuye con mejoras

---

**¡Disfruta descubriendo nuevas películas y series! 🍿🎬**
