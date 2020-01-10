import libreria

def agregarDirec():
    # 1. Pedir el direccion
    familia=libreria.pedir_nombre("Ingrese la familia:")
    direc=libreria.pedir_cadena("Ingrese el direccion:")
    # 2. Guardar la direccion en el archivo direc.txt
    contenido= familia+ "-" + direc + "\n"
    libreria.guardar_datos("direc.txt", contenido, "a")
    print("Datos guardados")

def mostrarDirec():
    # 1. Abrir el archivo direc.txt y mostrar sus datos
    data=libreria.obtener_datos_lista("direc.txt")
    # 2. Comprobar si hay datos
    if ( data != ""):
        for item in data:
            familia, direc = item.split("-")
            msg="La familia {} reside en la calle {}"
            familia=familia.replace("\n","")
            direc=direc.replace("\n","")
            print(msg.format(familia, direc))
        #fin_for
    else:
        print("No hay datos")

opc=""
max=3
while(opc != max):
    print("######### MENU ########")
    print("# 1. Agregar Direccion#")
    print("# 2. Mostrar Direccion#")
    print("# 3. Salir            #")
    print("#######################")
    opc=libreria.pedir_numero("Ingrese Opcion:", 1, 3)

    if ( opc ==1 ):
        agregarDirec()
    if ( opc ==2 ):
        mostrarDirec()
#fin_while
