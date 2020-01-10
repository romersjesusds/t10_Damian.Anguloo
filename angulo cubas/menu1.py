import libreria

def agregarDNI():
    # 1. Pedir el DNI
    nombre=libreria.pedir_nombre("Ingrese el nombre:")
    DNI=libreria.pedir_dni("Ingrese el DNI:")
    # 2. Guardar el DNI en el archivo dni.txt
    contenido=nombre + "-" + DNI + "\n"
    libreria.guardar_datos("dni.txt", contenido, "a")
    print("Datos guardados")

def mostrarDNI():
    # 1. Abrir el archivo dni.txt y mostrar sus datos
    data=libreria.obtener_datos_lista("dni.txt")
    # 2. COmprobar si hay datos
    if ( data != ""):
        for item in data:
            nombre, DNI = item.split("-")
            msg="La persona con nombre {} tiene un numero de DNI igual a {}"
            nombre=nombre.replace("\n","")
            DNI=DNI.replace("\n","")
            print(msg.format(nombre, DNI))
        #fin_for
    else:
        print("No hay datos")

opc=""
max=3
while(opc != max):
    print("######### MENU ########")
    print("# 1. Agregar DNI      #")
    print("# 2. Mostrar DNI      #")
    print("# 3. Salir            #")
    print("#######################")
    opc=libreria.pedir_numero("Ingrese Opcion:", 1, 3)

    if ( opc ==1 ):
        agregarDNI()
    if ( opc ==2 ):
        mostrarDNI()
#fin_while
