def test_sorted(tupla):
    if tupla == ():
        return -1
    anterior = tupla[0]
    for algo in tupla:
        if anterior <= algo:
            anterior = algo
        else:
            return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()