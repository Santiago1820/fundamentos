from datetime import date
import zood

# Preguntamos nuestra fecha
username = input("¿Cuál es tu nombre? ")
userbirthday = int(input("¿Cuál es tu dia de cumpleaños? "))
usermonth = int(input("¿Cuál es tu mes de cumpleaños? "))
useryear = int(input("¿Cuál es tu año de nacimiento? "))
print("Hola,", username)

# Declaramos nuestra variable edad apra obtener su edad
hoy = (date.today())
edad = (hoy - date(useryear, usermonth, userbirthday)).days // 365.27
edadd = (date(hoy))
edadm = (12-usermonth)+hoy.month
print ("Han pasado:", int(edad), "años", edadm, "meses", "y", edadd, "días desde que nacise hasta hoy: ", f"{hoy.day}/{hoy.month}/{hoy.year}")

#Traer el signo zoodiacal
print ("Tu signo es: ", zood.sigzood(userbirthday, usermonth))