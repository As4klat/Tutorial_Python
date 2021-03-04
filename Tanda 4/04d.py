def magnitude(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i] * x[i]
    return sum ** (1/2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()