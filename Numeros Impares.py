#jugadores = ("Juan", "Pedro", "Maria")
#for nom in jugadores:
#    print (nom)

'''
Cargar por teclado dos números, e imprimir los números impares
que se encuentran comprendidos entre ellos, en forma ascendente
y descendente.
'''
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numeros = numero1,numero2

if numero1 %2 == 0:
    impar = 2
else:
    impar = 2

for num in range(numero1,numero2,impar):
    print (num)