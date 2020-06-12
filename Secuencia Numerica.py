'''
Ingresar una secuencia de números, de a uno por vez, la carga finaliza
cuando el usuario ingresa el cero. Determinar

a) Porcentaje que representan los números divisibles por 3 sobre el total de
números ingresados en la secuencia

b) Determinar la cantidad de números que son el cuadrado del número anterior

c) Determinar la posición del mayor elemento impar de la secuencia
'''

suma, i = 0, 1
while i <= 5:
    n = int(input('Ingrese un número mayor a cero: '))
    if n <= 0:
        break
    suma += n
    i += 1
print('La suma de los números ingresados es:', suma)
if suma %3 ==0:
    div3 =

print(n)