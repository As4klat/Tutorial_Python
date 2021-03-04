compr = True

while compr:
    namigos = input("Introduce cuántos amigos tienes: ")
    try:
        namigos = int(namigos)
        compr = False
    except ValueError:
        print(namigos, "no es un número, prueba de nuevo")

for n in range(namigos):
    nombre = input("Introduce tu amigo: ")
    print("Hola amigo", nombre)