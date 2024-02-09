from datetime import date
import zood

# Preguntamos nuestra fecha
username = input("¿Cuál es tu nombre? ")
userbirthday = int(input("¿Cuál es tu dia de cumpleaños? "))
usermonth = int(input("¿Cuál es tu mes de cumpleaños? "))
useryear = int(input("¿Cuál es tu año de nacimiento? "))
print("Hola, ", username)

# Declaramos nuestra variable edad apra obtener su edad
edad = (date.today() - date(useryear, usermonth, userbirthday)).days // 365
edadd = (date.today() - edad * 12
edadm = edad * 12
print ("Tu edad es: ", edad, " años")
print ("Han pasado: ", edadd, " días")
print ("Han pasado: ", edadm, " meses")

#Traer el signo zoodiacal
print ("Tu signo es: ", zood.sigzood(userbirthday, usermonth))