compr = True
while compr:
    try:
        inicial = int(input("Valor inicial: "))
        final = int(input("Valor final  : "))
        compr = False
    except ValueError:
        print("Introduzca solo valores numéricos enteros\n")

inicial += inicial % 2
for i in range(inicial, final+1, 2):
    print(i)