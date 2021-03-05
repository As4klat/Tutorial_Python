def es_potencia_de_dos(n):
    while n != 1:
        if (n % 2) == 0:
            n = n / 2
        else:
            return False
    return True


def suma_potencias_de_2(a, b):
    suma = 0
    for n in range(a, b+1):
        if es_potencia_de_dos(n):
            suma += n
    return suma


print(suma_potencias_de_2(6, 15))
print(suma_potencias_de_2(17, 30))