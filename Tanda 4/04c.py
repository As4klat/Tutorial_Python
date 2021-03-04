def parallel(x, y):
    k = x[0]/y[0]
    for i in range(1, len(x)):
        if k != x[i]/y[i]:
            return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()