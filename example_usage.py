"""
Script de ejemplo para demostrar el sistema de recomendación
Ejecutar: python example_usage.py
"""

from recommendation_system import NetflixRecommendationSystem
import pandas as pd

def main():
    print("=" * 60)
    print("🎬 Netflix Recommendation System - Demo")
    print("=" * 60)
    
    # Inicializar el sistema
    print("\n📂 Cargando dataset...")
    recommender = NetflixRecommendationSystem('netflix_titles.csv')
    print("✓ Sistema listo!\n")
    
    # 1. Estadísticas
    print("📊 Estadísticas del Dataset:")
    print("-" * 60)
    stats = recommender.get_stats()
    for key, value in stats.items():
        print(f"  {key.replace('_', ' ').title()}: {value:,}")
    
    # 2. Búsqueda de títulos
    print("\n\n🔍 Buscando títulos con 'Breaking'...")
    print("-" * 60)
    search_results = recommender.search_titles("Breaking")
    print(search_results.to_string(index=False))
    
    # 3. Obtener recomendaciones
    print("\n\n🎯 Recomendaciones para 'Breaking Bad':")
    print("-" * 60)
    recommendations = recommender.get_recommendations("Breaking Bad", n_recommendations=5)
    
    if recommendations is not None:
        for idx, (_, row) in enumerate(recommendations.iterrows(), 1):
            print(f"\n{idx}. {row['title']}")
            print(f"   Tipo: {row['type']}")
            print(f"   Géneros: {row['listed_in']}")
            print(f"   Similitud: {row['similarity_score']*100:.1f}%")
            print(f"   📝 {row['description'][:100]}...")
    
    # 4. Filtrar por género
    print("\n\n🎭 Top 5 títulos de Drama:")
    print("-" * 60)
    drama = recommender.filter_by_genre("Drama", limit=5)
    print(drama.to_string(index=False))
    
    # 5. Trending
    print("\n\n📈 Top 5 Estrenos Recientes:")
    print("-" * 60)
    trending = recommender.get_trending(limit=5)
    print(trending.to_string(index=False))
    
    # 6. Filtrar por tipo
    print("\n\n🎥 Total de Películas vs Series:")
    print("-" * 60)
    movies = recommender.filter_by_type('Movie')
    tv_shows = recommender.filter_by_type('TV Show')
    print(f"  Películas: {len(movies):,}")
    print(f"  Series: {len(tv_shows):,}")
    
    print("\n" + "=" * 60)
    print("✓ Demo completada!")
    print("=" * 60)

if __name__ == "__main__":
    main()
