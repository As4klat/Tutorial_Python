def suma_divisores(n):
    suma = 1
    for i in range(2, n//2+1):
        if n % i == 0:
            suma += i


def perfecto(m):
    n = 1
    for i in range(m):
        while n != suma_divisores(n):
            n += 1
        print(n)
        n += 1


perfecto(5)