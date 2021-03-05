def suma_divisores(n):
    suma = 1
    for i in range(2, n//2+1):
        if n % i == 0:
            suma += i
    return suma


print(suma_divisores(6))
print(suma_divisores(1))
print(suma_divisores(0))