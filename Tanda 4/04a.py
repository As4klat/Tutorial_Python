def scalar(x, y):
    p = list()
    for i in range(len(x)):
        p.append(x[i]*y[i])
    return sum(p)


if __name__ == "__main__":
    import doctest
    doctest.testmod()