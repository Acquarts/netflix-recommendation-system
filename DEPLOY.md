# 🚀 Guía de Deploy - Netflix Recommendation System

## 📋 Resumen de Opciones de Deploy

| Plataforma | Dificultad | Costo | Configuración |
|-----------|-----------|-------|---------------|
| Streamlit Cloud | ⭐ Muy Fácil | Gratis | Automática |
| Heroku | ⭐⭐ Fácil | $5-7/mes | Semiautomática |
| AWS/GCP/Azure | ⭐⭐⭐ Moderada | Variable | Manual |
| DigitalOcean | ⭐⭐ Fácil | $5/mes | Manual |

---

## 🌟 Opción 1: Streamlit Cloud (RECOMENDADO)

La forma más fácil de deployar. Totalmente gratuita y con actualizaciones automáticas.

### Paso 1: Preparar tu Repositorio GitHub

```bash
# 1. Inicializar git en tu proyecto
git init

# 2. Crear archivo .gitignore
echo "
__pycache__/
*.pyc
venv/
.DS_Store
" > .gitignore

# 3. Hacer commit
git add .
git commit -m "Initial commit - Netflix Recommendation System"

# 4. Crear repositorio en GitHub
# - Ve a https://github.com/new
# - Crea un repositorio llamado "netflix-recommendation-system"
# - Copia el URL HTTPS

# 5. Agregar remote y hacer push
git remote add origin https://github.com/TU_USUARIO/netflix-recommendation-system.git
git branch -M main
git push -u origin main
```

### Paso 2: Deploy en Streamlit Cloud

1. **Ve a https://streamlit.io/cloud**

2. **Haz clic en "New app"**

3. **Configura el deploy:**
   - **Repository**: `TU_USUARIO/netflix-recommendation-system`
   - **Branch**: `main`
   - **Main file path**: `app.py`

4. **Haz clic en "Deploy"**

5. **Espera 2-3 minutos** mientras Streamlit construye y deploya tu app

6. **¡Listo!** Tu app estará disponible en `https://share.streamlit.io/TU_USUARIO/netflix-recommendation-system`

### Ventajas:
✅ Gratis  
✅ Muy fácil de configurar  
✅ Actualizaciones automáticas con cada push  
✅ URL personalizada  
✅ Manejo de SSL automático  

### Limitaciones:
⚠️ Recursos limitados (1 GB RAM)  
⚠️ Se detiene después de 1 hora sin uso  
⚠️ Comunidad compartida  

---

## 🦸 Opción 2: Heroku

Opción paga pero con más recursos. Requiere método de pago.

### Paso 1: Instalación del CLI de Heroku

```bash
# macOS
brew tap heroku/brew && brew install heroku

# Windows (descargar desde https://devcenter.heroku.com/articles/heroku-cli)

# Linux
curl https://cli-assets.heroku.com/install.sh | sh
```

### Paso 2: Crear Archivos Necesarios

```bash
# Archivo: Procfile
echo "web: streamlit run --server.port=\$PORT --server.address=0.0.0.0 app.py" > Procfile

# Archivo: runtime.txt
echo "python-3.11.0" > runtime.txt

# Archivo: setup.sh
cat > setup.sh << 'EOF'
mkdir -p ~/.streamlit/
echo "[server]
headless = true
port = \$PORT
enableCORS = false
" > ~/.streamlit/config.toml
EOF
```

### Paso 3: Deploy

```bash
# Login en Heroku
heroku login

# Crear la app
heroku create tu-app-name

# Hacer deploy
git push heroku main

# Ver logs
heroku logs --tail
```

### URL de tu app:
```
https://tu-app-name.herokuapp.com
```

---

## ☁️ Opción 3: Google Cloud Platform (GCP)

### Paso 1: Crear Proyecto

```bash
# Instalar Google Cloud SDK
# https://cloud.google.com/sdk/docs/install

gcloud init

# Crear proyecto
gcloud projects create netflix-recommendation

# Seleccionar proyecto
gcloud config set project netflix-recommendation
```

### Paso 2: Deploy a App Engine

```bash
# Crear archivo app.yaml
cat > app.yaml << 'EOF'
runtime: python39
entrypoint: streamlit run app.py

env_variables:
  PORT: "8080"
EOF

# Deploy
gcloud app deploy
```

---

## 🐳 Opción 4: Docker + DigitalOcean App Platform

### Paso 1: Crear Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
COPY netflix_titles.csv .

EXPOSE 8080

CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
```

### Paso 2: Crear .dockerignore

```
__pycache__
*.pyc
venv
.git
.gitignore
README.md
.DS_Store
```

### Paso 3: Deploy a DigitalOcean

```bash
# 1. Crear cuenta en https://www.digitalocean.com
# 2. Crear un Droplet (VM) Ubuntu 22.04
# 3. SSH en el Droplet
# 4. Clonar repositorio
# 5. Instalar Docker
# 6. Construir imagen
# 7. Ejecutar contenedor
```

---

## ✅ Checklist Pre-Deploy

- [ ] `requirements.txt` tiene todas las dependencias
- [ ] `app.py` es el archivo principal
- [ ] `netflix_titles.csv` está en el repositorio
- [ ] No hay rutas de archivos hardcodeadas
- [ ] El código funciona localmente
- [ ] `.gitignore` está configurado
- [ ] `.streamlit/config.toml` está presente
- [ ] No hay secretos (API keys) en el código

---

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'X'"
**Solución:** Asegúrate de que todas las dependencias estén en `requirements.txt`

```bash
pip freeze > requirements.txt
```

### "FileNotFoundError: netflix_titles.csv"
**Solución:** El archivo debe estar en el repositorio y en la misma carpeta que `app.py`

### La app se carga muy lentamente
**Solución:** El cálculo de similitud es pesado. Para Streamlit Cloud, considera:
- Guardar el modelo precalculado
- Usar una versión más pequeña del dataset

```python
# En recommendation_system.py
@st.cache_resource
def load_system():
    return NetflixRecommendationSystem('netflix_titles.csv')
```

### "Out of Memory"
**Solución:** Streamlit Cloud tiene 1GB de RAM. Si excedes:
- Reduce el tamaño del dataset
- Optimiza el cálculo de TF-IDF
- Considera Heroku o GCP

---

## 🔐 Variables de Entorno (si necesitas)

### En Streamlit Cloud:
1. Ve a tu app settings
2. Secrets (en el sidebar)
3. Agrega tus variables:
```toml
database_url = "..."
api_key = "..."
```

### En app.py:
```python
import streamlit as st
db_url = st.secrets["database_url"]
```

---

## 📊 Monitoreo Post-Deploy

- **Streamlit Cloud**: Monitor automático en tu dashboard
- **Heroku**: `heroku logs --tail`
- **GCP**: `gcloud app logs read`
- **DigitalOcean**: `docker logs <container_id>`

---

## 🔄 Actualizar tu App

### Streamlit Cloud:
```bash
git push origin main  # Automáticamente se redeploy
```

### Heroku:
```bash
git push heroku main
```

### GCP:
```bash
gcloud app deploy
```

---

## 💰 Costos Estimados

| Plataforma | Costo Mensual | Escalabilidad |
|-----------|---------------|---------------|
| Streamlit Cloud | $0 | Media |
| Heroku | $7 | Alta |
| GCP | $10-50 | Muy Alta |
| AWS | $5-100 | Muy Alta |
| DigitalOcean | $5 | Alta |

---

## 📞 Soporte

- **Streamlit Cloud**: https://discuss.streamlit.io
- **Heroku**: https://devcenter.heroku.com
- **GCP**: https://cloud.google.com/support
- **DigitalOcean**: https://www.digitalocean.com/support

---

## ✨ Tips Avanzados

### 1. CI/CD Automático
```yaml
# .github/workflows/deploy.yml
name: Deploy to Streamlit
on: [push]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Streamlit Cloud
        run: streamlit run app.py
```

### 2. Caché Local
```python
@st.cache_resource
def load_model():
    return NetflixRecommendationSystem('netflix_titles.csv')
```

### 3. Limitar Recursos en Streamlit
```toml
# .streamlit/config.toml
[server]
maxUploadSize = 200
enableXsrfProtection = true
```

---

¡Ahora estás listo para deployar! 🚀
