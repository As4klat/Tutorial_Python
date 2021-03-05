def par(n):
    return not (n % 2)

def primo(n):
    if not n:
        return False
    prim = True
    for i in range(2, int(n ** (1 // 2))):
        if not (n % i):
            prim = False
    return prim

if __name__ == "__main__":
    import doctest
    doctest.testmod()