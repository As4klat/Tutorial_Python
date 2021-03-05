def numMulFor(m, n):
    numMul = 0
    for i in range(m, n+1):
        if i % m == 0:
            numMul += 1
    return numMul


print(numMulFor(12, 360))