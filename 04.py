def fahrenheit_celsius(f):
    return (f - 32)*5/9


print("Grados Fahrenheit     Grados Celsius")
print("=================     ==============")
for f in range(0, 121, 10):
    print("      ", f, "            ", fahrenheit_celsius(f))