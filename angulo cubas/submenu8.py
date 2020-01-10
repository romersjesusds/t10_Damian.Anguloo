import libreria

def AgregarSubOpcionA():
    #1. pedir precio
    precio=libreria.pedir_precio("Ingrese precio : ",10,50)
    plato=libreria.pedir_nombre("Ingrese nombre : ")
    # 2. Guardar datos en pescados.txt
    contenido = plato + "-" + precio + "\n"
    libreria.agregar_datos("pescados.txt", contenido,"a")
    print("datos guardados")

def MostrarSubOpcionA():
    # 1. Abrir el archivo pescados.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("pescados.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            plato,precio = item.split("-")
            msg="El plato  {} cuesta  {} soles "
            precio=precio.replace("\n","")
            postre=postre.replace("\n","")
            print(msg.format(plato,precio))
        #fin_for
    else:
        print("No hay datos")

def AgregarSubOpcionB():
    # 1. pedir precio
    precio1 = libreria.pedir_precio("Ingrese precio : ")
    plato1 = libreria.pedir_nombre("Ingrese nombre : ")
    # 2. Guardar datos en criolla.txt
    contenido = plato1 + "-" + precio1 + "\n"
    libreria.agregar_datos("pescados.txt", contenido, "a")
    print("datos guardados")


def MostrarSubOpcionB():
    # 1. Abrir el archivo criolla.txt y mostrar sus datos
    datos = libreria.obtener_datos_lista("criolla.txt")
    # 2. Comprobar si hay datos
    if (datos != ""):
        for item in datos:
            plato1, precio1 = item.split("-")
            msg = "El plato  {} cuesta  {} soles "
            precio1 = precio1.replace("\n", "")
            postre1 = postre1.replace("\n", "")
            print(msg.format(plato1, precio1))
        # fin_for
    else:
        print("No hay datos")


def OpcionA():
    print("####### Pescados ########")
    print("#1. Agregar precio    #")
    print("#2. mostrar precio    #")
    print("#3. salir             #")
    print("#######################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarSubOpcionA()
    if(opc==2):
        MostrarSubOpcionA()
    #fin if
#fin while

def OpcionB():
    print("####### Criolla ########")
    print("#1. agregar precio        #")
    print("#2. mostrar precio        #")
    print("#3. salir                 #")
    print("###########################")
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
    print("###### Platos ######")
    print("#1. Pescados        #")
    print("#2. Criolla         #")
    print("#3. Salir           #")
    print("#####################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        OpcionA()
    if(opc==2):
        OpcionB()
    #fin if
#fin while
print("fin")
