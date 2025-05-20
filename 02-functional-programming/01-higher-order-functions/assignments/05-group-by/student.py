def group_by(xs, key_function):
    group = {}
    for item in xs:
        if not group.get(key_function(item), False):
            group[key_function(item)] = [item]
        else:
            group[key_function(item)].append(item)
