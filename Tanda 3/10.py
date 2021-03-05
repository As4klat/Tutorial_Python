i = 0
total = 0
while True:
    leyendo = True
    while leyendo:
        try:
            n = float(input("Introduzca un número :"))
            leyendo = False
        except ValueError:
            print("Introduzca un valor numérico")
    if n == -1:
        break
    else:
        total += n
        i += 1
print("Se ingresaron", i, "números que suman", total)
print("El promedio es de: ", total / i)