'''
Desarrolle un programa completo en Python, sin usar las funciones predefinidas min() y max(),
 que permita ingresar la cantidad de alumnos promocionados en los últimos 3 años de AED (un 0
 indica que ese año no hubo promocionados). Indicar cuál fue la mayor y cuál la menor cantidad
 de promocionados.  Indicar con un mensaje de “Revisar las condiciones de promoción” si en algún
 año NO hubo alumnos promocionados.
'''
#Datos del alumno:
#Francisco Massello 1k06 86246
#UTNFRC
#Ingreso de datos
print("----"*15)
print("AVISO: Este programa solo funciona con numeros mayores o iguales a cero")
print("----"*15)
prom2019 = int(input("Ingrese la cantidad de promocionados en el año 2019: "))
prom2018 = int(input("Ingrese la cantidad de promocionados en el año 2018: "))
prom2017 = int(input("Ingrese la cantidad de promocionados en el año 2017: "))
#Condicionales
if prom2018 <= prom2019 and prom2018 <= prom2017:
    menor = "En el año 2018 hubo menor cantidad de promocionados"
elif prom2019 <= prom2017 and prom2019 <= prom2018:
    menor = "En el año 2019 hubo menor cantidad de promocionados"
elif prom2017 <= prom2018 and prom2017 <= prom2019:
    menor = "En el año 2017 hubo menor cantidad de promocionados"

if prom2019 >= prom2017 and prom2019 >= prom2018:
    mayorprom = "En el año 2019 hubo mayor cantidad de promocionados"
elif prom2017 >= prom2019 and prom2017 >= prom2018:
    mayorprom = "En el año 2017 hubo mayor cantidad de promocionados"
elif prom2018 >= prom2019 and prom2018 >= prom2017:
    mayorprom = "En el año 2018 hubo mayor cantidad de promocionados"
#Resultados y condicionales
print("----"*15)
print("Resultados:")

if prom2019 == 0:
    print("\nAVISO: Revisar las condiciones de promoción en el año 2019")
if prom2018 == 0:
    print("\nAVISO: Revisar las condiciones de promoción en el año 2018")
if prom2017 == 0:
    print("\nAVISO: Revisar las condiciones de promoción en el año 2017")

print ("\n",mayorprom)
print ("\n",menor)
