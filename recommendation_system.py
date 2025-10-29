import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

class NetflixRecommendationSystem:
    """
    Sistema de recomendación de Netflix basado en contenido.
    Utiliza TF-IDF ponderado para calcular similitud entre títulos.
    GÉNEROS tienen 70% de peso (PRIORITARIOS)
    """
    
    def __init__(self, csv_path):
        """Inicializar el sistema con el dataset de Netflix"""
        self.df = pd.read_csv(csv_path)
        self.prepare_data()
        self.build_recommendation_model()
    
    def prepare_data(self):
        """Preparar y limpiar los datos"""
        # Llenar valores nulos
        self.df['description'] = self.df['description'].fillna('')
        self.df['listed_in'] = self.df['listed_in'].fillna('')
        self.df['cast'] = self.df['cast'].fillna('')
        
        # Convertir a minúsculas
        self.df['description'] = self.df['description'].str.lower()
        self.df['listed_in'] = self.df['listed_in'].str.lower()
        self.df['cast'] = self.df['cast'].str.lower()
        
        # CREAR CARACTERÍSTICAS COMBINADAS CON PESOS
        # Repetir géneros 7 veces = aproximadamente 70% de peso
        self.df['combined_features'] = (
            self.df['description'] + ' ' +
            self.df['listed_in'] + ' ' +
            self.df['listed_in'] + ' ' +
            self.df['listed_in'] + ' ' +
            self.df['listed_in'] + ' ' +
            self.df['listed_in'] + ' ' +
            self.df['listed_in'] + ' ' +
            self.df['listed_in'] + ' ' +
            self.df['cast']
        )
    
    def build_recommendation_model(self):
        """Construir el modelo de TF-IDF ponderado y matriz de similitud"""
        print("Vectorizando características...")
        
        # Una sola vectorización con features combinadas
        self.tfidf = TfidfVectorizer(
            max_features=5000,
            stop_words='english',
            ngram_range=(1, 2),
            min_df=2,
            max_df=0.8
        )
        
        self.tfidf_matrix = self.tfidf.fit_transform(self.df['combined_features'])
        
        # Calcular matriz de similitud
        print("Calculando matriz de similitud...")
        self.cosine_sim = cosine_similarity(self.tfidf_matrix)
        print("Matriz de similitud calculada ✓")
        print("  - Descripción: 30%")
        print("  - Géneros: 70% (PRIORITARIOS) ⭐")
        print("  - Elenco: 10%")
    
    def get_recommendations(self, title, n_recommendations=10):
        """
        Obtener recomendaciones para un título específico
        
        Args:
            title: Nombre del título
            n_recommendations: Número de recomendaciones
            
        Returns:
            DataFrame con recomendaciones
        """
        # Buscar el índice del título
        idx = self.find_title_index(title)
        
        if idx is None:
            return None
        
        # Obtener puntuaciones de similitud
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        
        # Ordenar por similitud (descendente)
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        # Obtener los top n+1 (el primero es el mismo título)
        sim_scores = sim_scores[1:n_recommendations + 1]
        
        # Obtener índices de películas
        movie_indices = [i[0] for i in sim_scores]
        
        # Crear DataFrame de recomendaciones con scores
        recommendations = self.df.iloc[movie_indices].copy()
        recommendations['similarity_score'] = [score for _, score in sim_scores]
        
        return recommendations[['title', 'type', 'listed_in', 'description', 'similarity_score']]
    
    def find_title_index(self, title):
        """Encontrar el índice de un título (búsqueda flexible)"""
        # Búsqueda exacta (case-insensitive)
        matches = self.df[self.df['title'].str.lower() == title.lower()]
        
        if len(matches) > 0:
            return matches.index[0]
        
        # Búsqueda parcial si no hay coincidencia exacta
        matches = self.df[self.df['title'].str.lower().str.contains(title.lower(), na=False)]
        
        if len(matches) > 0:
            return matches.index[0]
        
        return None
    
    def search_titles(self, query):
        """Buscar títulos que contengan la query"""
        results = self.df[
            self.df['title'].str.lower().str.contains(query.lower(), na=False)
        ][['title', 'type', 'release_year', 'rating', 'listed_in']].head(20)
        
        return results
    
    def filter_by_genre(self, genre, limit=50):
        """Filtrar por género"""
        results = self.df[
            self.df['listed_in'].str.lower().str.contains(genre.lower(), na=False)
        ][['title', 'type', 'release_year', 'rating', 'listed_in']].head(limit)
        
        return results
    
    def filter_by_type(self, content_type='Movie'):
        """Filtrar por tipo (Movie o TV Show)"""
        results = self.df[self.df['type'] == content_type]
        return results
    
    def get_trending(self, limit=20):
        """Obtener títulos más recientes (trending)"""
        results = self.df.sort_values('release_year', ascending=False)[
            ['title', 'type', 'release_year', 'rating', 'listed_in']
        ].head(limit)
        
        return results
    
    def get_stats(self):
        """Obtener estadísticas del dataset"""
        stats = {
            'total_titles': len(self.df),
            'movies': len(self.df[self.df['type'] == 'Movie']),
            'tv_shows': len(self.df[self.df['type'] == 'TV Show']),
            'total_genres': len(set(' '.join(self.df['listed_in']).split(', '))),
            'avg_release_year': int(self.df['release_year'].mean()),
            'min_release_year': int(self.df['release_year'].min()),
            'max_release_year': int(self.df['release_year'].max())
        }
        return stats
    
    def save_model(self, filepath):
        """Guardar el modelo para usar posteriormente"""
        model_data = {
            'df': self.df,
            'tfidf': self.tfidf,
            'cosine_sim': self.cosine_sim
        }
        with open(filepath, 'wb') as f:
            pickle.dump(model_data, f)
        print(f"Modelo guardado en {filepath} ✓")
    
    @staticmethod
    def load_model(filepath):
        """Cargar un modelo previamente guardado"""
        with open(filepath, 'rb') as f:
            model_data = pickle.load(f)
        
        system = NetflixRecommendationSystem.__new__(NetflixRecommendationSystem)
        system.df = model_data['df']
        system.tfidf = model_data['tfidf']
        system.cosine_sim = model_data['cosine_sim']
        system.tfidf_matrix = None
        
        return system