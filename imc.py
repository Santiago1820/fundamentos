from pesos import *

def menu(imc):
    if imc <= 18.5 :
         p_bajo()
    elif imc >= 18.5 and imc < 25:
        normal()
    elif imc >= 25 and imc < 30:
        s_peso()
    elif imc >= 30 and imc < 35:
        ob_leve()
    elif imc >= 35 and imc < 40:
        ob_media()
    else:
        if ob_alta():
            return True
while True:
    p = float(input("Ingresa tu peso en KG: "))
    a = float(input("Ingresa tu altura en metros: "))
    imc = p/(a*a)
    if menu(imc):
        break
    else:
        break

print("Tu IMC es:", imc)