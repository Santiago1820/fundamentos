inicial = 0 
cantiafaf = 0
ahorro = 0
objetivo = int(input("Cual es tu objetivo: "))

while inicial < 1:
    print ("Tu saldo es: ", ahorro)
    print ("selecciona una opcion:")
    print("1: ingresar dinero")
    print("2: retirar dinero")
    print("3: Salir")
    opcion = input()
    if opcion == "1":
        cantiadad = int(input ("Cuanto deseas añadir: ")) 
        ahorro = ahorro + cantiadad
    elif opcion == "2":
        cantiadad = int(input ("Cuanto deseas retirar: ")) 
        ahorro = ahorro - cantiadad
    if opcion == "3":
        break
    if ahorro == objetivo:
        print("Has llegado a tu meta",objetivo)
        break
    else:
        print("Esa opción no exite selecciona una opción correcta: ")