print("**********************")
print("Bienvenido a Rappy")
print("**********************")

nombre = input("Cuál es tu nombre? ")
clave = int(input("Cuál es tu clave de empleado? "))
antiguedad = int(input("Cuál es tu antiguedad? "))
vacaciones = 0

if(clave == 1):
    if(antiguedad == 1):
        vacaciones = 6
    elif(antiguedad >= 2 and antiguedad <= 6):
        vacaciones = 14
    elif(antiguedad >= 7):
        vacaciones = 20
elif(clave == 2):
    if(antiguedad == 1):
        vacaciones = 7
    elif(antiguedad >= 2 and antiguedad <= 6):
        vacaciones = 15
    elif(antiguedad >= 7):
        vacaciones = 22
elif(clave == 3):
    if(antiguedad == 1):
        vacaciones = 10
    elif(antiguedad >= 2 and antiguedad <= 6):
        vacaciones = 20
    elif(antiguedad >= 7):
        vacaciones = 30
        
print("Tienes", vacaciones, "días de vacaciones.")
