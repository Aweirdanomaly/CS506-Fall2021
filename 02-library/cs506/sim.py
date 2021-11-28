def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)


def manhattan_dist(x, y):
    res = 0.0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res


def jaccard_dist(x, y):
    if len(x) == 0 or len(y) == 0:
        raise ValueError("lengths must not be zero")

    large_size = max(len(x), len(y))

    # padding to the same size
    new_x = x + [0] * (large_size - len(x))
    new_y = y + [0] * (large_size - len(y))

    intersect = sum([1 if i == j else 0 for i, j in zip(new_x, new_y)])

    return 1 - intersect / large_size


def cosine_sim(x, y):
    if x == [] or y == []:
        raise ValueError("lengths must not be zero")
    elif len(x) != len(y):
        raise ValueError("lengths must be equal")

    dot_prod = sum(abs(val1*val2) for val1, val2 in zip(x, y))

    x_len = (sum(el**2 for el in x))**(1/2)
    y_len = (sum(el**2 for el in y))**(1/2)

    cos = dot_prod/(x_len * y_len)

    return cos

# Feel free to add more
