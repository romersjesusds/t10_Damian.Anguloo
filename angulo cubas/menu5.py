import libreria

def agregarPrecio():
    # 1. Pedir el Precio
    marca=libreria.pedir_nombre("Ingrese la marca de zapatilla:")
    precio=libreria.pedir_precio_zapa("Ingrese el precio:",50,500)
    # 2. Guardar la direccion en el archivo precio.txt
    contenido= marca+ "-" + precio + "\n"
    libreria.guardar_datos("precio.txt", contenido, "a")
    print("Datos guardados")

def mostrarPrecio():
    # 1. Abrir el archivo precio.txt y mostrar sus datos
    data=libreria.obtener_datos_lista("precio.txt")
    # 2. COmprobar si hay datos
    if ( data != ""):
        for item in data:
            marca, precio = item.split("-")
            msg="La zapatilla de marca {} cuesta {} soles"
            marca=marca.replace("\n","")
            precio=precio.replace("\n","")
            print(msg.format(marca,precio))
        #fin_for
    else:
        print("No hay datos")

opc=""
max=3
while(opc != max):
    print("######### MENU ########")
    print("# 1. Agregar Precio   #")
    print("# 2. Mostrar Preci    #")
    print("# 3. Salir            #")
    print("#######################")
    opc=libreria.pedir_numero("Ingrese Opcion:", 1, 3)

    if ( opc ==1 ):
        agregarPrecio()
    if ( opc ==2 ):
        mostrarPrecio()
#fin_while
