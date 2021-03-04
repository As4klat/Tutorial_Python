def fahrenheit_celsius(f):
    return (f - 32)*5/9


compr = True
while compr:
    try:
        faren = float(input("Introduzca temperatura en grados Fahrenheit: "))
        compr = False
    except ValueError:
        print("Introduzca un valor numérico\n")


print("La temperatura equivalente en grados Celsius es :",
      fahrenheit_celsius(faren))