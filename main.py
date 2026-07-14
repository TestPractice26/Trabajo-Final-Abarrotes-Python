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