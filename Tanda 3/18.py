def dia_semana(dia):
    semana = dia % 7
    if semana == 0:
        return "domingo"
    elif semana == 1:
        return "lunes"
    elif semana == 2:
        return "martes"
    elif semana == 3:
        return "miércoles"
    elif semana == 4:
        return "jueves"
    elif semana == 5:
        return "viernes"
    else:
        return "sabado"


if __name__ == '__main__':
    import doctest
    doctest.testmod()