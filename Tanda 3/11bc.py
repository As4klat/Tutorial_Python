def num_mul(m, n):
    i = 1
    mul = m
    while mul <= n:
        i += 1
        mul *= i
    return (i-1)


print(num_mul(12, 360))