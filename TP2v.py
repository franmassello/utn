# TP 02 - Generación Estadísticas COVID-19
# 2020_AED_TP2_Beato_L[1k6]_Massello_L[1k6]_Revol_86335_[1k2]
# División subproblemas


def caracter_arroba(mail):
    valido = False
    conta_arroba = 0
    if mail[0] == "@" or mail[-1] == "@":
        return valido
    for car in mail:
        if car == "@":
            conta_arroba += 1
    if conta_arroba == 0 or conta_arroba < 1 or conta_arroba > 1:
        return valido
    valido = True
    return valido


def puntos_seguidos(mail):
    valido = False
    anterior = None
    for punto in mail:
        actual = punto
        if actual == "." and anterior == ".":
            return valido
        else:
            anterior = actual
    valido = True
    return valido


def regla_punto(mail):
    valido = False
    if mail[0] == "." or mail[-1] == ".":
        return valido
    valido = True
    return valido


def validacion_mail():
    mail = input("Ingrese su mail: ")
    salir = True
    intentos = 3
    correcto = False
    while salir:
        if caracter_arroba(mail):
            if puntos_seguidos(mail):
                if regla_punto(mail):
                    print("El mail ingresado ha sido correcto.")
                    correcto = True
                else:
                    print("El mail ingresado fue incorrecto, revise que no "
                          "empiece ni termine con un punto")
                    intentos -= 1
                    print("Le quedan", intentos, "intentos")
            else:
                print("El mail ingresado fue incorrecto, revise que no tenga "
                      "dos puntos seguidos.")
                intentos -= 1
                print("Le quedan", intentos, "intentos")
        else:
            print("El mail ingresado fue incorrecto, revise que UN caracter "
                  "'@' en la posición intermedia del mismo.")
            intentos -= 1
            print("Le queda/n", intentos, "intento/s")
        if correcto:
            return
        if intentos == 0:
            salir = False
        else:
            mail = input("Ingrese nuevamente su mail: ")
    print("El mail se ha ingresado TRES veces de manera incorrecta, se"
          "procederá a salir")


def principal():
    validacion_mail()


principal()

# 1. Validación de Mail
#   a. Tener un sólo caracter @ en una posición intermedia de la cadena (ni la
#   primera ni la última letra)
#   b. No contener dos puntos seguidos (uno a continuación del otro)
#   c. No empezar ni terminar con un punto
#   d. Si la cuenta ingresada es inválida, se debe permitir el reingreso de la
#   misma. Luego de tres intentos incorrectos, el programa debe detener la
#   ejecución.
# 2. Generación Aleatoria de Datos de n pacientes
#   a. Edad
#   b. Resultado del test (positivo/negativo)
#   c. Región (Capital, Gran Córdoba, Norte y Sur)
#   d. Si tuvo contacto con casos confirmados
#   e. Si es personal de salud
#   f. Si viajo al exterior
#   g. Determinar automáticamente si es caso autóctono
# (Se considera un caso autóctono si el resultado del test fue positivo y NO
# estuvo en contacto con casos confirmados, NO es personal de salud y NO viajó
# al exterior.)
# 3. Menú de Opciones que permita informar
#   a. Cantidad de casos confirmados (test positivo) y porcentaje sobre el
#   total de casos.
#   b. Edad promedio de los pacientes que pertenecen a grupo de riesgo (para
#   pertenecer al grupo de riesgo el test debe ser negativo y tener más de 60
#   años).
#   c. Cantidad y porcentaje que el personal de salud representa sobre el
#   total de casos.
#   d. Edad promedio entre los casos confirmados.
#   e. Menor edad entre los casos autóctonos.
#   f. Cantidad de casos confirmados por región y porcentaje que representa
#   cada uno sobre el total de casos.
#   g. Cantidad de casos confirmados con viaje al exterior.
#   h. Cantidad de casos sospechosos en contacto con casos confirmados.
#   i. Las regiones sin casos confirmados.
#   j. Porcentaje de casos positivos autóctonos sobre el total de positivos.
