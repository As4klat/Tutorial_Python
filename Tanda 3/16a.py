def maxmin(a, b, c):
    if a > 0:
        return (-(b**2)/(4*a) + c, "máximo")
    else:
        return (-(b**2)/(4*a) + c, "mínimo")


(valor, Mm) = maxmin(-1, 1, 1)
print("Es un", Mm, "y su valor es", valor)