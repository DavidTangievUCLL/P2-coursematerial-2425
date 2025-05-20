from util import Card

def genres(movies):
    return {genre_item for movie in movies for genre_item in movie.genres}


def actors(movies):
    return {actor for movie in movies for actor in movie.actors}


def repeat_consecutive(xs, n):
    return [xs_item for xs_item in xs for i in range(n)]


def repeat_alternating(xs, n):
    return [xs_item for i in range(n) for xs_item in xs]


def cards(value, suits):
    return {Card(card, suit_item) for card in value for suit_item in suits}