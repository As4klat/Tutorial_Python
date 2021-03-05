def examen(numEje, porcentaje):
    while True:
        leyendo = True
        while leyendo:
            try:
                resueltos = float(input("Número de ejercicios resueltos",
                                        "(-1 para terminar): "))
                leyendo = False
            except ValueError:
                print("Introduzca una cantidad numérica")
        if resueltos == -1:
            return
        else:
            nota = 100/numEje * resueltos
            print("El % de ejercicios resueltos es", 100/numEje * resueltos)
            if nota < porcentaje:
                print("Suspendido")
            else:
                print("Aprobado")


examen(50, 25)