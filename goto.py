def diferente():
    print("este es una opcon que no esta en el menu")

def incio():
    print("Este es el inicio")

def final():
    print ("este es el final")
    return True

def otra():
    print ("Esta es otra opción")
    diferente()

while True:
    r = input ("¿quieres ir al inicio? (s/x/n)")
    if r == "s":
        incio()

    elif r == "x":
        otra()
        break

    else:
        final()
        break 

test = input("Escribe algo: ")
print (test)