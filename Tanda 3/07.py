def euclides(m, n):
    if m < n:
        cambio = m
        m = n
        n = cambio
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
    return n


print(euclides(15, 9), euclides(9, 15), euclides(10, 8), euclides(12, 6))