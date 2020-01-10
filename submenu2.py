import libreria

def AgregarSubOpcionA():
    #1. pedir brillo
    #2. Guardadr datos en brillo.txt
    brillo=libreria.pedir_numero("Ingrese brillo: ",1,100)
    contenido =str(brillo) + "\n"
    libreria.agregar_datos("brillo.txt", contenido,"a")
    print("nuevo brillo guardado")

def MostrarSubOpcionA():
    # 1. Abrir el archivo brillo.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("brillo.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
         brillo=libreria.mostrar_datos("brillo.txt")
         msg="brillo.. {} %"
         brillo=brillo.replace("\n","")
         print(msg.format(brillo))
         #fin_for
    else:
        print("No hay datos")

def AgregarSubOpcionB():
    #1. pedir brillo
    #2. Guardadr datos en brillo.txt
    brillo=libreria.pedir_numero("Ingrese brillo: ",1,100)
    contenido =str(brillo) + "\n"
    libreria.agregar_datos("brillo.txt", contenido,"a")
    print("nuevo brillo guardado")


def MostrarSubOpcionB():
     # 1. Abrir el archivo brillo.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("brillo.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
         brillo=libreria.mostrar_datos("brillo.txt")
         msg="brillo.. {} % " + "\n"
         brillo=brillo.replace("\n","")
         print(msg.format(brillo))
         #fin_for
    else:
        print("No hay datos")



def OpcionA():
    print("########## CAMARA TRASERA ##########")
    print("#1. AGREGAR brillo                 #")
    print("#2. MOSTRAR brillo                 #")
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
    print("##### CAMARA FRONTAL ########")
    print("#1. Agregar BRILLO          #")
    print("#2. mostrar BRILLO          #")
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
    print("#1. CAMARA TRASERA            #")
    print("#2. CAMARA FRONTAL            #")
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
