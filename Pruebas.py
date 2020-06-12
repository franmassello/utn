
#generacion de datos
pacientes = 0
contador_pacientes = 0
contador_casosconfirmados = 0
import random
pacientes = input("Ingrese la cantidad de pacientes a analizar: ")
while pacientes != 0:
    contador_pacientes += 1
    edad = random.randint(0,120)

    test = random.randint(1,2)
    if test == 1:
        testfinal = "Resultado del test: positivo"
        contador_casosconfirmados +=1
    if test == 2:
        testfinal = "Resultado del test: negativo"

    region = random.randint(0,3)
    if region == 0:
        region = "Region: Capital"
    if region == 1:
        region = "Region: Gran Cordoba"
    if region == 2:
        region = "Region: Norte"
    if region == 3:
        region = "Region: Sur"

    contacto = random.randint(0,1)
    if contacto == 0:
        contacto = "Contacto con casos confirmados: Si"
    if contacto == 1:
        contacto = "Contacto con casos confirmados: No"

    personal = random.randint(0,1)
    if personal == 0:
        personal = "Es personal de la salud: Si"
    if personal == 1:
        personal = "Es personal de la salud: No"

    viajo = random.randint(0,1)
    if viajo == 0:
        viajo = "Viajo: Si"
    if viajo == 1:
        viajo = "Viajo: No"

    if test == 1 and contacto == 1 and personal == 1 and viajo == 1:
        caso_sospechoso = "si Es caso sospechoso"
    else:
        caso_sospechoso = "No es caso sospechoso"
    todos = (testfinal, region, contacto, personal, viajo, caso_sospechoso)











