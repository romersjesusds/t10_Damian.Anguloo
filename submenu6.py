import libreria

def AgregarSubOpcionA():
    #1. pedir estado
    #2. Guardadr datos en estados.txt
    estados=libreria.pedir_cadena("Ingrese estado: ")
    fecha=libreria.pedir_numero("ingrese fecha:",1,31)
    contenido= estados + "-" + str(fecha) + "\n"
    libreria.agregar_datos("estados.txt", contenido,"a")
    print("estado nuevo guardado")
    print("se envio estadoa todos sus amigos de whatsapp")

def MostrarSubOpcionA():
    # 1. Abrir el archivo estados.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("estados.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
         for item in datos:
            estado, fecha= item.split("-")
            msg="el estado '{}' se cambió hoy {} del presente mes"
            estado=estado.replace("\n","")
            fecha=fecha.replace("\n","")
            print(msg.format(estado, str(fecha)))
        #fin_for
    else:
        print("No hay datos")

def AgregarSubOpcionB():
    #1. pedir estado
    #2. Guardadr datos en estados.txt
    estados=libreria.pedir_cadena("Ingrese estado: ")
    fecha=libreria.pedir_numero("ingrese fecha:",1,31)
    contenido =estados + "-" + str(fecha) + "\n"
    libreria.agregar_datos("estados.txt", contenido,"a")
    print("estado nuevo guardado")
    print("se envio estadoa todos sus amigos de facebook")


def MostrarSubOpcionB():
    # 1. Abrir el archivo estados.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("estados.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
         for item in datos:
            estado, fecha= item.split("-")
            msg="el estado '{}' se cambió hoy {} del presente mes"
            estado=estado.replace("\n","")
            fecha=fecha.replace("\n","")
            print(msg.format(estado, str(fecha)))
        #fin_for
    else:
        print("No hay datos")





def OpcionA():
    print("########## WHATSAPP ##########")
    print("#1. AGREGAR ESTADO                 #")
    print("#2. MOSTRAR ESTADOS                 #")
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
    print("##### FACEBOOK ########")
    print("#1. Agregar ESTADO          #")
    print("#2. mostrar ESTADO          #")
    print("#3. salir                   #")
    print("#############################")
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
    print("#1. whatsapp            #")
    print("#2. facebook            #")
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
