def grad_c():
    g_f1 = (grados * 9/5) + 32
    g_k1 = grados + 273.15
    g_r1 = (grados * 1.8) + 491.67
    print(f"°F = {g_f1}, °K = {g_k1}, °R = {g_r1}")

def grad_f():
    g_c2 = (grados - 32) * 5/9
    g_k2 = (grados - 32) * 5/9 + 273.15 
    g_r2 = grados + 459.67
    print(f"°C = {g_c2}, °K = {g_k2}, °R = {g_r2}")

def grad_k():
    g_f3 = (grados - 273.15) * 9/5 + 32
    g_c3 = grados - 273.15
    g_r3 = grados * 9/5
    print(f"°F = {g_f3}, °C = {g_c3}, °R = {g_r3}")

def grad_r():
    g_f4 = grados - 459.67
    g_k4 = grados * 5/9
    g_c4 = (grados - 491.67) * 5/9
    print(f"°F = {g_f4}, °K = {g_k4}, °C = {g_c4}")

def menu(r):
    if r == "c":
        grad_c()
    elif r == "f":
        grad_f()
    elif r == "k":
        grad_k()
    else:
        if grad_r():
            return True

while True:
    grados = float(input("Escribe el numero de grados que tienes "))
    print("Selecciona solo la letra para saber que tipo de ° tienes:")
    r = input("°C, °F, °K, °R: ")
    if menu(r):
        break
    else:
        break