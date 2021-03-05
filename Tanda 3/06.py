from random import randrange

n = randrange(10)
while True:
    compr = True
    while compr:
        try:
            adivina = int(input("Adivina el número: "))
            compr = False
        except ValueError:
            print("Introduzca un valor numérico")
    if adivina == n:
        print("¡¡ Ese es !!")
        break
    elif adivina < n:
        print("El número es más alto")
    else:
        print("El número es más bajo")