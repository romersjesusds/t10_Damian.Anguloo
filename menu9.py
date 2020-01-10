import libreria

def AgregarPrecio():
    # 1. Pedir producto
    # 2. Pedir precio
    # 3. Guardar datos en precios.txt
    producto=libreria.pedir_nombre("Ingrese producto: ")
    precio=libreria.pedir_entero("ingrese precio:")
    contenido = producto + "-" + "s/." + str(precio) + "\n"
    libreria.agregar_datos("precios.txt", contenido,"a")
    print("se agrego el precio de un nuevo producto")

def MostrarPrecios():
    # 1. Abrir el archivo precios.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("precios.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            producto, precio= item.split("-")
            msg="{} cuesta {} nuevo(s) sol(es)" \
                ""
            producto=producto.replace("\n","")
            precio=precio.replace("\n","")
            print(msg.format(producto, precio))
        #fin_for
    else:
        print("sin datos")



opc=""
max=3
while(opc!=max):
    print("############### MENU ##############")
    print("#1. Agregar precio de producto    #")
    print("#2. Mostrar precios               #")
    print("#3. Salir                         #")
    print("###################################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarPrecio()
    if(opc==2):
        MostrarPrecios()
    #fin if
#fin while
print("fin")
