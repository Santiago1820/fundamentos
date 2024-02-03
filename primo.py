n = int(input("Ingresa un número entero "))
primo = True
for i in range(2,n):
    if n % i==0:
        primo=False
        break
if primo:
    print("Es primo")
else:
    print("No es primo")
