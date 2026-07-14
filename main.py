from datetime import datetime, timedelta

def validarTextoNoVacio(mensaje): #valida que se haya ingresado texto
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Error: Este campo es obligatorio.\n")

def validarEnteroPos(minimo, mensaje): #valida que el dato ingresado sea un numero entero positivo
    while True:
        try:
            numero = int(input(mensaje))
            if numero >= minimo:
                return numero
            else:
                print(f"Error: Debe ser mayor o igual a {minimo}.\n")
        except ValueError:
            print("Error: Ingrese un número entero válido.\n")

def validarRealPos(minimo, mensaje): #valida que el dato ingresado se un numero real positivo
    while True:
        try:
            numero = float(input(mensaje))
            if numero >= minimo:
                return round(numero, 2)
            else:
                print(f"Error: Debe ser mayor o igual a {minimo}.\n")
        except ValueError:
            print("Error: Ingrese un número real válido.\n")

def validarFecha(mensaje):
    while True:
        texto = input(mensaje).strip()
        try:
            fecha = datetime.strptime(texto, "%d-%m-%Y")
            return fecha
        except ValueError:
            print("Fecha inválida. Use el formato dd-mm-aaaa \n")

def validarOpciones(mensaje, opcionesValidas):
    while True:
        valor = input(mensaje).strip().lower()
        if valor in opcionesValidas:
            return valor
        print(f"Opción incorrecta. Escriba una de las siguientes: {", ".join(opcionesValidas)}. \n")