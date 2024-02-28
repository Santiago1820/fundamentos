import math

def main():
    print("¿Qué cuerpo geométrico circular deseas calcular?")
    print("1. Esfera")
    print("2. Cilindro")
    print("3. Cono")
    opcion = input("Ingresa el número de la opción deseada: ")

    if opcion == "1":
        calcular_area_volumen("esfera")
    elif opcion == "2":
        calcular_area_volumen("cilindro")
    elif opcion == "3":
        calcular_area_volumen("cono")


def calcular_area_volumen(opcion):
    if opcion == "esfera":
        area = 4 * math.pi * radio ** 2
        volumen = (4/3) * math.pi * radio ** 3
        radio = float(input("Ingresa el radio de la esfera: "))
        print("El área de la esfera es:", area)
        print("El volumen de la esfera es:", volumen)

    
    
    elif opcion == "cilindro":
        radio = float(input("Ingresa el radio de la base del cilindro: "))
        altura = float(input("Ingresa la altura del cilindro: "))
        area = 2 * math.pi * radio * (radio + altura)
        volumen = math.pi * radio ** 2 * altura
        print("El área del cilindro es:", area)
        print("El volumen del cilindro es:", volumen)
    else:
        radio = float(input("Ingresa el radio de la base del cono: "))
        altura = float(input("Ingresa la altura del cono: "))
        generatriz = math.sqrt(radio ** 2 + altura ** 2)
        area = math.pi * radio * (radio + generatriz)
        volumen = (1/3) * math.pi * radio ** 2 * altura
        print("El área del cono es:", area)
        print("El volumen del cono es:", volumen)

main()