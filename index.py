from datetime import date
username = input("¿Cuál es tu nombre?")
userbirthday = int(input("¿Cuál es tu dia de cumpleaños?"))
usermonth = int(input("¿Cuál es tu mes de cumpleaños?"))
useryear = int(input("¿Cuál es tu año de nacimiento?"))

print("Hola, " + username)

edad = (date.today() - date(useryear, usermonth, userbirthday)).days // 365

print (edad)