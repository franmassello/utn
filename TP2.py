import random
# TP 02 - Generación Estadísticas COVID-19
# 2020_AED_TP2_Beato_86278_[1k6]_Massello_86246_[1k6]_Revol_86335_[1k2]
# División subproblemas


def caracter_arroba(mail):
    valido = False
    conta_arroba = 0
    if mail == "":
        return valido
    if mail[0] == "@" or mail[-1] == "@":
        return valido
    for car in mail:
        if car == "@":
            conta_arroba += 1
    if conta_arroba < 1 or conta_arroba > 1:
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
    mail = input("\033[1;96mPara comenzar, ingrese su mail: ")
    salir = True
    intentos = 3
    correcto = False
    while salir:
        if caracter_arroba(mail):
            if puntos_seguidos(mail):
                if regla_punto(mail):
                    print("\033[1;36mEl mail ingresado ha sido correcto.")
                    correcto = True
                else:
                    print("\033[1;93mEl mail ingresado fue incorrecto, revise"
                          " que no empiece ni termine con un punto.")
                    intentos -= 1
                    print("\033[1;31mLe queda/n", intentos, "intento/s")
            else:
                print("\033[1;93mEl mail ingresado fue incorrecto, revise que "
                      "no tenga dos puntos seguidos.")
                intentos -= 1
                print("\033[1;31mLe queda/n", intentos, "intento/s")
        else:
            print("\033[1;93mEl mail ingresado fue incorrecto, revise que haya"
                  " UN caracter '@' en la posición intermedia del mismo.")
            intentos -= 1
            print("\033[1;31mLe queda/n", intentos, "intento/s")
        if correcto:
            return
        if intentos == 0:
            salir = False
        else:
            mail = input("\033[1;96mIngrese nuevamente su mail: ")
    print("\033[1;31mEl mail se ha ingresado TRES veces de manera incorrecta, "
          "se procederá a salir.")
    exit()


def print_menu():
    print("\033[1;96m=" * 18, "\033[1;34mMenu de Opciones", "\033[1;96m=" * 18)
    print("\033[1;96m1.\033[1;36m Cantidad de casos confirmados y "
          "porcentaje total")
    print("\033[1;96m2.\033[1;36m Edad promedio de los pacientes que "
          "pertenecen a grupo de riesgo")
    print("\033[1;96m3.\033[1;36m Cantidad y porcentaje que el personal "
          "de salud representa sobre el total de casos.")
    print("\033[1;96m4.\033[1;36m Edad promedio entre los casos confirmados")
    print("\033[1;96m5.\033[1;36m Menor edad entre los casos autóctonos")
    print("\033[1;96m6.\033[1;36m Cantidad de casos confirmados por región y "
          "porcentaje que representa cada uno sobre el total de casos")
    print("\033[1;96m7.\033[1;36m Cantidad de casos confirmados con "
          "viaje al exterior")
    print("\033[1;96m8.\033[1;36m Cantidad de casos sospechosos en "
          "contacto con casos confirmados")
    print("\033[1;96m9.\033[1;36m Regiones sin casos confirmados")
    print("\033[1;96m10.\033[1;36m Porcentaje de casos positivos autóctonos")
    print("\033[1;96m0.\033[1;36m Salir del programa")


# ///// PROGRAMA /////
print("\033[1;34m=" * 60)
print("\033[1;34m=" * 4, "\033[1;36mBienvenido al Generador de Estadísticas de"
                         " COVID-19", "\033[1;34m=" * 3)
print("\033[1;34m=" * 60)

validacion_mail()

t_casos = int(input("\033[1;96mIngrese la cantidad de pacientes de los cuales"
                    " desea generar datos: "))
print("\033[1;31mProcesando...")

# ///// GENERACIÓN DE DATOS /////
# Nota - la sigla "t" representa total y La sigla "c" representa confirmado.
# Variables relacionadas a la Edad
t_mayor = 0
t_edad_c = 0
t_edad_riesgo = 0
# Variables relacionadas al diagnóstico
t_confirmado = 0
t_salud = 0
t_viaje = 0
t_contacto = 0
t_autoctono = 0
# Variables relacionadas a la localidad
capital = 0
gran_cordoba = 0
norte = 0
sur = 0
# Variables relacionadas a las preguntas del menú
min_edad_a = 121
viaje_c = 0
capital_c = 0
gran_cordoba_c = 0
norte_c = 0
sur_c = 0

for paciente in range(t_casos):
    confirmado = False
    viaje = False
    autoctono = 0
    edad = random.randint(0, 120)
    if edad >= 60:
        t_mayor += 1
        t_edad_riesgo += edad
    resultado_test = random.randint(1, 3)
    if resultado_test == 1:
        t_confirmado += 1
        confirmado = True
    region = random.randint(1, 4)
    if region == 1:
        capital += 1
        if confirmado:
            capital_c += 1
    elif region == 2:
        gran_cordoba += 1
        if confirmado:
            gran_cordoba_c += 1
    elif region == 3:
        norte += 1
        if confirmado:
            norte_c += 1
    elif region == 4:
        sur += 1
        if confirmado:
            sur_c += 1
    contacto_casos = random.randint(1, 2)
    if contacto_casos == 1:
        t_contacto += 1
    else:
        autoctono += 1
    salud = random.randint(1, 3)
    if salud == 1:
        t_salud += 1
    else:
        autoctono += 1
    viaje = random.randint(1, 3)
    if viaje == 1:
        viaje = True
        t_viaje += 1
    else:
        autoctono += 1
    if confirmado:
        t_edad_c += edad
        if viaje:
            viaje_c += 1
        if autoctono == 3:
            if edad < min_edad_a:
                min_edad_a = edad
            t_autoctono += 1
# ///// PROCESO DE DATOS /////

prom_edad_riesgo = t_edad_riesgo / t_mayor
prom_edad_c = t_edad_c / t_casos
porc_confirmados = t_confirmado*100 / t_casos
porc_salud = t_salud*100 / t_casos
porc_capital = capital_c*100 / t_casos
porc_g_cordoba = gran_cordoba_c*100 / t_casos
porc_norte = norte_c*100 / t_casos
porc_sur = sur_c*100 / t_casos
porc_autoctono = t_autoctono*100 / t_casos
t_region_c = capital_c + gran_cordoba_c + norte_c + sur_c

print("\033[1;93mLos datos fueron procesados con éxito. Accediendo al menú")
for i in range(30000000):
    pass
print_menu()
entrada = True
while entrada:
    menu = 1
    if menu != 0:
        menu = int(input("\033[1;96m¿Qué información desea consultar? "
                         "(Escriba el número correspondiente): "))
    if menu == 0:
        print("¡Gracias por utilizar nuestro programa!")
        exit()
    elif menu == 1:
        print("\033[1;34mLa cantidad de casos confirmados es de", t_confirmado)
        print("Esto representa un", round(porc_confirmados), "% sobre el total"
                                                             " de casos.")
    elif menu == 2:
        print("\033[1;34mLa edad promedio de los pacientes pertenecientes "
              "al grupo de riesgo es de", round(prom_edad_riesgo), "años.")
    elif menu == 3:
        print("\033[1;34mLa cantidad de pacientes que son personal"
              " de salud es de", t_salud, "\nEsto representa un",
              round(porc_salud), "% sobre el total de casos.")
    elif menu == 4:
        print("\033[1;34mLa edad promedio entre los casos confirmados es de",
              round(prom_edad_c), "años.")
    elif menu == 5:
        print("\033[1;34mLa menor edad entre los casos autóctonos "
              "es de", min_edad_a, "años.")
    elif menu == 6:
        print("\033[1;34mLa cantidad de casos confirmados por región"
              " es la siguiente:")
        print("\033[1;93mCapital:\033[1;31m", capital_c,
              "Caso/s | " "\033[1;34mEsto representa un",
              round(porc_capital), "% del total.")
        print("\033[1;93mGran Córdoba:\033[1;31m", gran_cordoba_c,
              "Caso/s | " "\033[1;34mEsto representa un",
              round(porc_g_cordoba), "% del total.")
        print("\033[1;93mNorte:\033[1;31m", norte_c,
              "Caso/s | " "\033[1;34mEsto representa un",
              round(porc_norte), "% del total.")
        print("\033[1;93mSur:\033[1;31m", sur_c,
              "Caso/s | ", "\033[1;34mEsto representa un",
              round(porc_sur), "% del total")
    elif menu == 7:
        print("\033[1;34mLa cantidad de casos confirmados con viaje al"
              " exterior es de:", viaje_c)
    elif menu == 8:
        print("\033[1;34mLa cantidad de casos sospechosos en "
              "contacto con casos confirmados es de", t_contacto)
    elif menu == 9:
        if t_region_c == 0:
            print("\033[1;34mNinguna región tiene casos confirmados.")
        else:
            if capital_c and gran_cordoba and norte_c and sur_c > 0:
                print("\033[1;31mNo hay ninguna región SIN casos confirmados.")
            if capital_c == 0:
                print("\033[1;34mNo hay casos confirmados en Capital.")
            if gran_cordoba_c == 0:
                print("\033[1;34mNo hay casos confirmados en Gran Córdoba.")
            if norte_c == 0:
                print("\033[1;34mNo hay casos confirmados en el Norte.")
            if sur_c == 0:
                print("\033[1;34mNo hay casos confirmados en el Sur.")
    elif menu == 10:
        print("\033[1;34mEl porcentaje de casos positivos autóctonos es de",
              round(porc_autoctono), "%")
    if 0 <= menu <= 10:
        salir = input("\033[1;96m¿Desea consultar otra opción? (Si/No): ")
        if salir.lower() == "no":
            entrada = False
        else:
            ver_menu = input("\033[1;96m¿Desea ver nuevamente el menú de"
                             " opciones? (Si/No): ")
            if ver_menu.lower() == "si":
                print_menu()
    if menu > 10 or menu < 0:
        print("\033[1;31mEl número ingresado no corresponde a ninguna"
              " de las opciones disponibles, intente nuevamente.")