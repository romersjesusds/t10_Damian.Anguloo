import libreria

def AgregarSubOpcionA():
    #1. pedir contraseña
    #2. Guardadr datos en conexiones.txt
    contrasenia=libreria.pedir_cadena("Ingrese contraseña:")
    conexion=libreria.pedir_cadena("ingrese medio de conexion:")
    contenido =contrasenia + "-" + conexion + "\n"
    libreria.agregar_datos("conexiones.txt", contenido,"a")
    print("coxexion guardada")
    print("conectando")

def MostrarSubOpcionA():
    # 1. Abrir el archivo conexiones.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("conexiones.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
         for item in datos:
            contrasenia, conexion= item.split("-")
            msg="te conectaste a {} con la contraseña '{}'"
            contrasenia=contrasenia.replace("\n","")
            conexion=conexion.replace("\n","")
            print(msg.format(contrasenia, conexion))
        #fin_for
    else:
        print("No hay datos")

def AgregarSubOpcionB():
    #1. pedir contraseña
    #2. Guardadr datos en conexiones.txt
    contrasenia=libreria.pedir_cadena("Ingrese contraseña:")
    conexion=libreria.pedir_cadena("ingrese medio de conexion:")
    contenido =contrasenia + "-" + conexion + "\n"
    libreria.agregar_datos("conexiones.txt", contenido,"a")
    print("coxexion guardada")
    print("conectando")


def MostrarSubOpcionB():
    # 1. Abrir el archivo conexiones.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("conexiones.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
         for item in datos:
            contrasenia, conexion= item.split("-")
            msg="te conectaste a {} con la contraseña '{}'"
            contrasenia=contrasenia.replace("\n","")
            conexion=conexion.replace("\n","")
            print(msg.format(conexion, contrasenia))
        #fin_for
    else:
        print("No hay datos")


def OpcionA():
    print("########## wifi ##########")
    print("#1. AGREGAR contraseña             #")
    print("#2. MOSTRAR contraseña             #")
    print("#3. salir                          #")
    print("####################################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarSubOpcionA()
    if(opc==2):
        MostrarSubOpcionA()
    #fin if
#fin while

def OpcionB():
    print("##### bluetooh ########")
    print("#1. Agregar contraseña #")
    print("#2. mostrar contraseña #")
    print("#3. salir              #")
    print("########################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarSubOpcionB()
    if(opc==2):
        MostrarSubOpcionB()
    #fin if
#fin while

opc=""
max=3
while(opc!=max):
    print("############ MENU #############")
    print("#1. conectar WIFI             #")
    print("#2. conectar BLUETOOTH        #")
    print("#3. Salir                     #")
    print("###############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        OpcionA()
    if(opc==2):
        OpcionB()
    #fin if
#fin while
print("fin")
