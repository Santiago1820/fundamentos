inicial = 0 
ahorro = 0
objetivo = int(input("Cual es tu objetivo: "))

while inicial < 1:
    print ("Tu saldo es: ", ahorro, "\nSelecciona una opcion:\n1: ingresar dinero\n2: retirar dinero\n3: Salir")
    opcion = input()
    if opcion == "1":
        cantiadad = int(input ("Cuanto deseas añadir: ")) 
        ahorro = ahorro + cantiadad
    elif opcion == "2":
        cantiadad = int(input ("Cuanto deseas retirar: ")) 
        if cantiadad > ahorro:
            print("No puedes retirar más de lo que tienes")
        else:
            ahorro = ahorro - cantiadad
    elif opcion == "3":
        break
    else:
        print("Esa opción no exite selecciona una opción correcta: ")
    
    if ahorro >= objetivo:
        print("Has llegado a tu meta",objetivo)
        break      