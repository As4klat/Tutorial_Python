def triangular_iterativo(n):
    triangular = 0
    for i in range(1, n+1):
        triangular += i
    return triangular


def triangular_calculado(n):
    return int(n * (n+1)/2)


compr = True
while compr:
    try:
        n = int(input("Introducir número triangulo: "))
        compr = False
    except ValueError:
        print("Solo valores numéricos\n")

for i in range(1, n+1):
    triangular_iterativo(i)


print("Ya")

for i in range(1, n+1):
    triangular_calculado(i)

print("Otro ya")