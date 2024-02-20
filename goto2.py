def diferente():
    print("Esta es una opción que no está en el menú")

def inicio():
    print("Este es el inicio")

def final():
    print("Este es el final")
    return True

def otra():
    print("Esta es otra opción")
    diferente()

def menu(r):
    if r == "s":
        inicio()
    elif r == "x":
        otra()
    else:
        if final():
            return True

while True:
    r = input("¿Quieres ir al inicio? (s/x/n)")
    if menu(r):
        break