print("Introducir notas")
print("------------------------")
i = 0
total = 0
compr = True
while compr:
    leyendo = True
    while leyendo:
        try:
            n = float(input("Introduzca nota : "))
            leyendo = False
        except ValueError:
            print("Introduzca un valor numérico")
    total += n
    i += 1
    leyendo = True
    while leyendo:
        respuesta = input("¿Otra nota? (S/N)")
        if (respuesta in "SNsn") and len(respuesta) == 1:
            leyendo = False
    if respuesta in "Nn":
        compr = False
print("Promedio de: ", total / i, " puntos")