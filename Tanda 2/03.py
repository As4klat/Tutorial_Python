def mayor_producto(n1, n2, n3, n4):
    mayor = n1 * n2
    n1n3 = n1 * n3
    n1n4 = n1 * n4
    n2n3 = n2 * n3
    n2n4 = n2 * n4
    n3n4 = n3 * n4
    if n1n3 > mayor:
        mayor = n1n3
    if n1n4 > mayor:
        mayor = n1n4
    if n2n3 > mayor:
        mayor = n2n3
    if n2n4 > mayor:
        mayor = n2n4
    if n3n4 > mayor:
        mayor = n3n4
    return mayor

if __name__ == '__main__':
    import doctest
    doctest.testmod()