import random

# Agente humanizado que recomienda películas
def agente_recomendador_peliculas():
    # Diccionario de películas organizadas por género
    peliculas_por_genero = {
        "acción": ["Duro de matar", "John Wick", "Busqueda Implacable", "Gladiador", "Misión Imposible"],
        "comedia": ["Supercool", "Que paso ayer", "Deadpool", "Son como niños", "Guerra de papas"],
        "drama": ["Forrest Gump", "El Padrino", "Titanic", "El castor", "El Club de la Pelea"],
        "ciencia ficción": ["Inception", "Blade Runner ", "Interstellar", "Matrix", "Star Wars"],
        "terror": ["El Exorcista", "Hereditary", "El conjuto", "It", "Ultimo Exorcismo"]
    }
    
    # Presentación del agente
    print("¡Hola! me llamo Felix y soy un agente para recomendación de películas. 😊")
    print("Te ayudaré a encontrar una película perfecta para ti.")
    
    # Solicitar el género favorito al usuario
    genero = input("¿Cuál es tu género de película favorito? (acción, comedia, drama, ciencia ficción, terror): ").strip().lower()
    
    # Verificar si el género existe en el diccionario
    if genero in peliculas_por_genero:
        # Seleccionar una película aleatoria del género
        pelicula_recomendada = random.choice(peliculas_por_genero[genero])
        print(f"\n¡Excelente! Te recomiendo la película: '{pelicula_recomendada}'. 🎬")
        print("Espero que la disfrutes. ¡Dime luego qué te pareció! 😄")
    else:
        print("\nLo siento, no tengo recomendaciones para ese género. 😢")
        print("¿Podrías intentar con otro género? (acción, comedia, drama, ciencia ficción, terror)")

# Ejecutar el agente
agente_recomendador_peliculas()