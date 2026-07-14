from datetime import datetime, timedelta

FormatoFecha = "%d/%m/%Y"
StockMinimo = 5
DiasAlertaVencimiento = 7


# funciones de validación
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
            fecha = datetime.strptime(texto, FormatoFecha)
            return fecha
        except ValueError:
            print("Fecha inválida. Use el formato dd/mm/aaaa (ejemplo: 18/07/2027) \n")

def validarOpciones(mensaje, opcionesValidas):
    while True:
        valor = input(mensaje).strip().lower()
        if valor in opcionesValidas:
            return valor
        print(f"Opción incorrecta. Escriba una de las siguientes: {", ".join(opcionesValidas)}. \n")

# funciones para el registro de productos (HU01)

def codigoExiste(productos, codigo):
    for prod in productos:
        if prod["codigo"] == codigo:
            return True
    return False

def registrarProductos(productos):
    print("\n" + 20*"-" + "Registrar nuevo Producto" + 10*"-")
    val = "s"
    while val == "s":
        while True:
            codigo = validarTextoNoVacio("Ingrese el código del producto (ej: P001): ").upper()
            if not codigoExiste(productos,codigo):
                break
            print("Este código ya esta registrado. \n")

        nombre = validarTextoNoVacio("Ingrese nombre del producto: ").capitalize()
        cantidad = validarEnteroPos(0,"Ingrese la cantidad: ")
        fechaVenc = validarFecha("ingrese fecha de vencimiento (dd/mm/aaaa)")

        nuevoProducto = {
            "codigo": codigo,
            "nombre": nombre,
            "cantidad": cantidad,
            "vencimiento": fechaVenc
        }
        productos.append(nuevoProducto)
        print(f"Producto '{nombre}' registrado correctamente. \n")

        val = validarOpciones("¿Desea registrar otro producto? (s = SI, n = NO)",["s","n"])
    return productos


# Funciones de Movimiento de almacen HU02

def buscarProductoCodigo(productos, codigo):
    for prod in productos:
        if prod["codigo"] == codigo:
            return prod
    return None

def registrarMov(productos, historial):
    print("\n" + 10*"-" + "REGISTRO DE MOVIMIENTO E/S" + 10*"-")

    if not productos:
        print("No hay productos registrados. \n")
        return
    
    val = "s"
    while val == "s":
        codigo = validarTextoNoVacio("igrese codigo de producto a buscar: ").upper()
        produto = buscarProductoCodigo(productos, codigo)

        if produto is None:
            print("No hay productos registrado con el codigo dado. \n")
        else:
            tipoM = validarOpciones("¿Tipo de movimiento a realizar? (e = entrada, s = salida): ", ["e","s"])
            cantMo = validarEnteroPos(1, "Ingrese la cantidad: ")

            if tipoM == "e":
                produto["cantidad"] += cantMo
                print(f"Entrada de stock registrada. El nuevo stock de {produto['nombre']} es {produto["cantidad"]} \n")
            else:
                producto["cantidad"] -= cantMo
                print(f"Salida de stock registrada. El nuevo stock de {produto['nombre']} es {produto["cantidad"]} \n")

        movimiento = {
            "fecha": datetime.now().strptime(FormatoFecha),
            "codigo": produto["codigo"],
            "nombre": produto["nombre"],
            "tipoMovimiento": tipoM,
            "cantidad": cantMo
        }
        historial.append(movimiento)

    val = validarOpciones("¿Desea registrar otro movimiento (s = si, n = no)?: ",["s", "n"])


