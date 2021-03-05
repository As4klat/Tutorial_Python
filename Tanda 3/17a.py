def bisiesto(anio):
    if anio % 4:
        return False
    else:
        if anio % 100:
            return True
        else:
            if anio % 400:
                return False
            else:
                return True


print(bisiesto(2017), bisiesto(2016), bisiesto(1800), bisiesto(2000))