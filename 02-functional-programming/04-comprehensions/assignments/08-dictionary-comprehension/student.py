def title_to_director(movies):
    return {movie.title: movie.director for movie in movies}

def director_to_titles(movies):
    return {movie2.director: [movie.title for movie in movies if movie.director == movie2.director] for movie2 in movies}