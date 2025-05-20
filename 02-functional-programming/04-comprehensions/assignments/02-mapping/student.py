from movie import *

def titles(movies: list[object]):
    collection = [movie.title for movie in movies]
    return collection

def titles_and_years(movies):
    collection = [(movie.title, movie.year) for movie in movies]
    return collection

def titles_and_actor_counts(movies):
    collection = [(movie.title, len(movie.actors)) for movie in movies]
    return collection

def reverse_words(sentence):
    if len(sentence) == 0:
        return ''
    return " ".join([word[::-1] for word in sentence.split()])