def sum(a, b):
    return a + b

def hms_seg(h, m, s):
    return ((h*60)+m)*60+s

def seg_hms(s):
    horas = s//3600
    s = s % 3600
    minutos = s//60
    segundos = s % 60
    return (horas, minutos, segundos)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

print(sum(2,3))