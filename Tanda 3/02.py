def abs(n):
    if n < 0:
        n = -n
    return n

if __name__ == '__main__':
    import doctest
    doctest.testmod()