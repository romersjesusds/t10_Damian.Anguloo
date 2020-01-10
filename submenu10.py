import libreria

def AgregarSubOpcionA():
    #1. pedir desayuno
    #2. pedir costo
    #3. Guardadr datos en desayuno.txt
    desayuno=libreria.pedir_nombre("Ingrese desayuno: ")
    costo=libreria.pedir_real("Ingrese costo: ")
    contenido = desayuno + "-" + str(costo) + "\n"
    libreria.agregar_datos("desayuno.txt", contenido,"a")
    print("se guardó un nuevo desayuno")


def MostrarSubOpcionA():
    # 1. Abrir el archivo desayuno.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("desayuno.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            desayuno, costo= item.split("-")
            msg="'{}' esta a solo S/. {} nuevos soles"
            desayuno=desayuno.replace("\n","")
            costo=costo.replace("\n","")
            print(msg.format(desayuno, str(costo)))
        #fin_for
    else:
        print("No hay datos")

def AgregarSubOpcionB():
    #1. pedir almuerzo
    #2. pedir costo
    #3. Guardadr datos en Almuerzo.txt
    almuerzo=libreria.pedir_nombre("Ingrese almuerzo: ")
    costo=libreria.pedir_real("Ingrese costo: ")
    contenido = almuerzo + "-" + str(costo) + "\n"
    libreria.agregar_datos("Almuerzo.txt", contenido,"a")
    print("se guardó un nuevo almuerzo")


def MostrarSubOpcionB():
    # 1. Abrir el archivo almuerzo.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("Almuerzo.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            almuerzo, costo= item.split("-")
            msg="'{}' esta a solo S/. {} nuevos soles"
            almuerzo=almuerzo.replace("\n","")
            costo=costo.replace("\n","")
            print(msg.format(almuerzo, str(costo)))
        #fin_for
    else:
        print("No hay datos")



def OpcionA():
    print("##### DESAYUNO ########")
    print("#1. Agregar DESAYUNO     #")
    print("#2. Mostrar DESAYUNO     #")
    print("#3. salir                  #")
    print("#############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarSubOpcionA()
    if(opc==2):
        MostrarSubOpcionB()
    #fin if
#fin while

def OpcionB():
    print("########### ALMUERZO ###########")
    print("#1. AGREGAR ALMUERZO           #")
    print("#2. MOSTRAR ALMUERZO           #")
    print("#3. salir                      #")
    print("################################")
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
    print("#1. desayuno           #")
    print("#2. almuerzo            #")
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
