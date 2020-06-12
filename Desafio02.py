"""
n = int(input("Ingrese el numero a calcular: "))
inicialn = n
print(inicialn)
longitud = 0
lista = [0]

while n != 1:
    while n%2 == 0:
        n = n/2
        longitud += 1
        print(n)
        if n == 1:
            print("La longitud de orbita es:", longitud)
            exit()
        else:
            continue

    while n%2 != 0:
        n = 3*n+1
        longitud += 1
        print(n)
        if n == 1:
            print("La longitud de orbita es:", longitud)

            exit()
        else:
            continue
"""


#TODO: Validar que exista valor ingresado y sea >=1
#lista = [0]

n = int(input("Ingrese el numero a calcular: "))
print(n)
longitud = 1
promedio = n
maximo = n

while n > 1:
    if n%2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1
    promedio += n
    longitud += 1
    if n>maximo:
        maximo=n
    print(n)

print("La longitud de orbita es:", longitud)
print("El promedio es:", promedio/longitud)
print("El maximo es:", maximo)

