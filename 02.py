def interes_compuesto(ci, x, n):
    return ci * (1 + x / 100) ** n


compr = True
while compr:
    try:
        capital = float(input("Introduce el capital inicial: "))
        anios = float(input("Introduce los años  : "))
        interes = float(input("Introduce el interés (%): "))
        compr = False
    except ValueError:
        print("Error en la introducción de datos\n")

print("Total a pagar: ", interes_compuesto(
    capital, interes, anios), "euros")