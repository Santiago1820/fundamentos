def sigzood(dia, mes):
    signo = ""
    if mes == 1:
        if dia <= 20:
            signo = "Capricornio"
        else:
            signo = "Acuario"
    elif mes == 2:
        if dia <= 18:
            signo = "Acuario"
        else:
            signo = "Piscis"
    elif mes == 3:
        if dia <= 20:
            signo = "Piscis"
        else:
            signo = "Aries"
    elif mes == 4:
        if dia <= 20:
            signo = "Aries"
        else:
            signo = "Tauro"
    elif mes == 5:
        if dia <= 21:
            signo = "Tauro"
        else:
            signo = "Géminis"
    elif mes == 6:
        if dia <= 21:
            signo = "Géminis"
        else:
            signo = "Cáncer"
    elif mes == 7:
        if dia <= 22:
            signo = "Cáncer"
        else:
            signo = "Leo"
    elif mes == 8:
        if dia <= 23:
            signo = "Leo"
        else:
            signo = "Virgo"
    elif mes == 9:
        if dia <= 23:
            signo = "Virgo"
        else:
            signo = "Libra"
    elif mes == 10:
        if dia <= 23:
            signo = "Libra"
        else:
            signo = "Escorpio"
    elif mes == 11:
        if dia <= 22:
            signo = "Escorpio"
        else:
            signo = "Sagitario"
    elif mes == 12:
        if dia <= 21:
            signo = "Sagitario"
        else:
            signo = "Capricornio"
    return signo
