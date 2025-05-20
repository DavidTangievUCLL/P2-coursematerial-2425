def directors(movies):
    if len(movies) == 0:
        return set()
    return set([movie.director for movie in movies])


def common_elements(xs, ys):
    return set([item for item in xs if item in xs and item in ys])
