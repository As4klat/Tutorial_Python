def astro(dia, mes):
    if mes == 1:
        if dia >= 21:
            return "Acuario"
        else:
            return "Capricornio"
    elif mes == 2:
        if dia >= 20:
            return "Piscis"
        else:
            return "Acuario"
    elif mes == 3:
        if dia >= 21:
            return "Aries"
        else:
            return "Piscis"
    elif mes == 4:
        if dia >= 21:
            return "Tauro"
        else:
            return "Aries"
    elif mes == 5:
        if dia >= 22:
            return "Géminis"
        else:
            return "Tauro"
    elif mes == 6:
        if dia >= 22:
            return "Cáncer"
        else:
            return "Géminis"
    elif mes == 7:
        if dia >= 24:
            return "Leo"
        else:
            return "Cáncer"
    elif mes == 8:
        if dia >= 24:
            return "Virgo"
        else:
            return "Leo"
    elif mes == 9:
        if dia >= 24:
            return "Libra"
        else:
            return "Virgo"
    elif mes == 10:
        if dia >= 24:
            return "Escorpio"
        else:
            return "Libra"
    elif mes == 11:
        if dia >= 23:
            return "Sagitario"
        else:
            return "Escorpio"
    elif mes == 12:
        if dia >= 22:
            return "Capricornio"
        else:
            return "Sagitario"


print(astro(5, 6), astro(29, 12), astro(23, 2),
      astro(15, 4), astro(29, 5), astro(13, 5))