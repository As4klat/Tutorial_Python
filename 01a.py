import doctest

'''
n: es el numero que se incrementa
range: es el rango del "10" que entra hasta el "21" que este ultimo no entra.
            [10,21)
'''

for n in range(10, 21):
    print(n)

doctest.testmod()