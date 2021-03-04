from "01.py"
import seg_hms, hms_seg

compr = True
while compr:
    try:
        h1 = int(input("Introduce horas    1: "))
        m1 = int(input("Introduce minutos  1: "))
        s1 = int(input("Introduce segundos 1: "))
        h2 = int(input("Introduce horas    2: "))
        m2 = int(input("Introduce minutos  2: "))
        s2 = int(input("Introduce segundos 2: "))
        compr = False

    except ValueError:
        print("Error en la introducción de datos, son datos numericos\n")

(h, m, s) = seg_hms(hms_seg(h1, m1, s1) + hms_seg(h2, m2, s2))

print("La suma es:", h, "horas", m, "minutos y", s, "segundos")