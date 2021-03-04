'''
Apartado 1
'''

def norma(x, y):
    return (x*x + y*y)**(1/2)

'''
Apartado 2
'''

def resta(x1, y1, x2, y2):
    return (x1-x2, y1-y2)

'''
Apartado 3
'''

def distancia(x1, y1, x2, y2):
    (x, y) = resta(x1, y1, x2, y2)
    return norma(x, y)

'''
Apartado 4
'''

def vector_unitario(x, y):
    n = norma(x, y)
    return (x/n, y/n)

'''
Apartado 5
'''

def vector_unitario2(x1, y1, x2, y2):
    (x, y) = resta(x2, y2, x1, y1)
    return vector_unitario(x, y)

'''
Apartado 6
'''

def proyeccion(x, y, dx, dy, cx, cy):
    (t1, t2) = resta(x, y, cx, cy)
    p11 = dx*dx
    p12 = dx*dy
    p21 = p12
    p22 = dy*dy
    rx = p11*t1 + p12*t2
    ry = p21*t1 + p22*t2
    rx += cx
    ry += cy
    return (rx, ry)

'''
Apartado 7
'''

def area_triangulo(b, h):
    return b*h/2

'''
Apartado 8
'''

def area_vectorial(x1, y1, x2, y2, x3, y3):
    (dos_uno_x, dos_uno_y) = resta(x2, y2, x1, y1)
    (dos_tres_x, dos_tres_y) = resta(x3, y3, x1, y1)
    area = dos_uno_x*dos_tres_y - dos_uno_y*dos_tres_x
    if area < 0:
        area = -area
    return area/2


def area_proyeccion(x1, y1, x2, y2, x3, y3):
    base = distancia(x1, y1, x3, y3)
    (dx, dy) = vector_unitario2(x1, y1, x3, y3)
    (px, py) = proyeccion(x2, y2, dx, dy, x3, y3)
    altura = distancia(x2, y2, px, py)
    return area_triangulo(base, altura)



print(6 / (area_proyeccion(0, 0, 2, 0, 1 ,2)  - 2))


print(6 / (area_vectorial(0, 0, 2, 0, 1 ,2) - 2))