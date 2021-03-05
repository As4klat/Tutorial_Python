def primos(n):
    print(1)
    if n >= 2:
        print(2)
    for i in range(3, n+1):
        primo = True
        for j in range(2, i):
            if i % j == 0:
                primo = False
                break
        if primo:
            print(i)

if __name__ == "__main__":
    import doctest
    doctest.testmod()