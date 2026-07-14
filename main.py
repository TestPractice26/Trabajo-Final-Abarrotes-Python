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
                print(f"Entrada de stock registrada. El nuevo stock de {produto['nombre']} es {produto['cantidad']} \n")
            else:
                producto["cantidad"] -= cantMo
                print(f"Salida de stock registrada. El nuevo stock de {produto['nombre']} es {produto['cantidad']} \n")

        movimiento = {
            "fecha": datetime.now().strptime(FormatoFecha),
            "codigo": produto["codigo"],
            "nombre": produto["nombre"],
            "tipoMovimiento": tipoM,
            "cantidad": cantMo
        }
        historial.append(movimiento)

    val = validarOpciones("¿Desea registrar otro movimiento (s = si, n = no)?: ",["s", "n"])


# Funciones de Algoritmo de Alertas HU03

def genAlerta(produtos):
    print("\n" + 50*"=")
    print("ALERTAS DEL SISTEMA")
    print("="*50)

    hoy = datetime.now()
    alerta = False

    for prod in produtos:
        # alerta de stok minimo
        if prod["cantidad"] <= StockMinimo:
            print(f"STOCK POR DEBAJO DE {StockMinimo} unidades. {prod['nombre']} ({prod['codigo']}): quedan {prod['cantidad']} unidades")
            alerta = True

        # alerta de vencimieto
        diasParaVenc = (prod["vencimiento"] - hoy).days
        if 0 <= diasParaVenc <= DiasAlertaVencimiento:
            print(f"CERCA A LA FECHA DE VENCIMIENTO {prod['nombre']} ({prod['codigo']}): vence en {diasParaVenc} dia(s) "
                  f"{prod['vencimiento'].strftime(FormatoFecha)}")
            alerta = True
        elif diasParaVenc < 0:
            print(f"PRODUCTO VENCIDO {prod['nombre']} ({prod['codigo']}); vencio el {prod['vencimiento'].strftime(FormatoFecha)}.")
            alerta = True

    if not alerta:
        print("No hay alertas activas.")
    print(50*"=")

# Funciones de Salidas de Datos HU04
def mostrarProd(productos):
    print("\n" + 100*"=")
    print(f"{'CODIGO':<10}{'NOMBRE':<20}{'STOCK':<10}{'Precio (S/.)':<15}{'VENCIMIENTO':<15}")
    print(100*"=")

    if not productos:
        print("No hay productos registrados. ")
    else:
        for prod in productos:
            print(f"{pro['codigo']:<10}{prod['nombre']:<20}{prod['cantidad']:<10}{prod['precio']:<15.2f}{prod['vencimiento'].strftime(FormatoFecha):<15}")
    print(100*"=")

def mostrarHistorial(historial):
    print("\n" + 100*"=")
    print(f"{'FECHA':<12}{'CODIGO':<10}{'PRODUCTO':<20}{'TIPO DE MOVIMIENTO':<15}{'CANTIDAD':<10}")
    print(100*"=")
    if not historial:
        print("Aún no se han registrado movimientos E/S.")
    else:
        for mov in historial:
            print(f"{mov['fecha']:<12}{mov['codigo']:<10}{mov['nombre']:<20}{mov['tipoMovimiento']:<15}{mov['cantidad']:<10}")
    print(100*"=")

# FUNCION MENU
def Menu():
    print("\n" + 70 * "#")
    print("GESTION DE STOCK Y CADUCIDAD DE ABARROTES")
    print(70 * "#")
    print("Opcion 1 = Registrar Producto")
    print("Opcion 2 = Registrar Movimiento (Entrda / Salida)")
    print("Opcion 3 = Mostrar lista de Productos")
    print("Opcion 4 = Mostral Historial de movimientos")
    print("Opcion 5 = Mostrar alertas (Stock bajo / Fecha de vencimiento proxima)")
    print("Opcion 6 = SALIR")
    print(70 * "#")

    while True:
        try:
            opcion = int(input("Elija una opcion (1-6): "))
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("Opcion invalida. Elija un numero entre 1 y 6")
        except ValueError:
            print("entrada inválida. Ingrese un numero")

