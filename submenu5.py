import libreria

def AgregarSubOpcionA():
    #1. pedir ARCHIVO
    #2. Guardadr datos en archivos.txt
    archivo=libreria.pedir_cadena("Ingrese msg: ")
    disco=libreria.pedir_nombre("Ingrese disco de llegada: ")
    contenido = archivo + "-" + disco + "\n"
    libreria.agregar_datos("archivos.txt", contenido,"a")
    print("archivo de texto nuevo guardado")

def MostrarSubOpcionB():
    # 1. Abrir el archivo archivos.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("archivos.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            archivo, disco= item.split("-")
            msg="el texto '{}' se guardo en {}"
            archivo=archivo.replace("\n","")
            disco=disco.replace("\n","")
            print(msg.format(archivo, disco))
        #fin_for
    else:
        print("No hay datos")

def AgregarSubOpcionC():
    #1. pedir ARCHIVO
    #2. Guardadr datos en archivos.txt
    archivo=libreria.pedir_cadena("Ingrese msg: ")
    disco=libreria.pedir_nombre("Ingrese disco de llegada: ")
    contenido = archivo + "-" + disco + "\n"
    libreria.agregar_datos("archivos.txt", contenido,"a")
    print("archivo de texto nuevo guardado")


def MostrarSubOpcionC():
    # 1. Abrir el archivo archivos.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("archivos.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            archivo, disco= item.split("-")
            msg="el texto '{}' se guardo en {}"
            archivo=archivo.replace("\n","")
            disco==disco.replace("\n","")
            print(msg.format(archivo, disco))
        #fin_for
    else:
        print("No hay datos")



def OpcionA():
    print("##### MEMORIA INTERNA ########")
    print("#1. Agregar  ARCHIVOS     #")
    print("#2. mostrar ARCHIVOS       #")
    print("#3. salir                   #")
    print("#############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarSubOpcionA()
    if(opc==2):
        MostrarSubOpcionB()
    #fin if
#fin while

def OpcionB():
    print("##### MICRO CD ########")
    print("#1. agregar ARCHIVOS     #")
    print("#2. mostrar ARCHIVOS       #")
    print("#3. salir                   #")
    print("#############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarSubOpcionC()
    if(opc==2):
        MostrarSubOpcionC()
    #fin if
#fin while

opc=""
max=3
while(opc!=max):
    print("############ MENU #############")
    print("#1. MEMORIA INTERNA            #")
    print("#2. MICRO CD              #")
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
