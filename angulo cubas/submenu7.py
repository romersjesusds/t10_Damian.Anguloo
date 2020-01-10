import libreria

def AgregarSubOpcionA():
    #1. pedir precio
    precio=libreria.pedir_precio("Ingrese precio : ",10,50)
    postre=libreria.pedir_nombre("Ingrese nombre : ")
    # 2. Guardar datos en frios.txt
    contenido = postre + "-" + precio + "\n"
    libreria.agregar_datos("frio.txt", contenido,"a")
    print("datos guardados")

def MostrarSubOpcionA():
    # 1. Abrir el archivo frio.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("frio.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            postre,precio = item.split("-")
            msg="El postre frio {} cuesta  {} soles "
            precio=precio.replace("\n","")
            postre=postre.replace("\n","")
            print(msg.format(postre,precio))
        #fin_for
    else:
        print("No hay datos")

def AgregarSubOpcionB():
    # 1. pedir precio
    precio1 = libreria.pedir_precio_postre("Ingrese precio : ")
    postre1 = libreria.pedir_nombre("Ingrese nombre : ")
    # 2. Guardar datos en calido.txt
    contenido = postre1 + "-" + precio1 + "\n"
    libreria.agregar_datos("calido.txt", contenido, "a")
    print("datos guardados")

def MostrarSubOpcionB():
    # 1. Abrir el archivo calido.txt y mostrar sus datos
    datos = libreria.obtener_datos_lista("calido.txt")
    # 2. Comprobar si hay datos
    if (datos != ""):
        for item in datos:
            postre1, precio1 = item.split("-")
            msg = "El postre calido {} cuesta  {} soles "
            precio = precio.replace("\n", "")
            postre = postre.replace("\n", "")
            print(msg.format(postre1, precio1))
        # fin_for
    else:
        print("No hay datos")


def OpcionA():
    print("####### Frios ########")
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
    print("####### Calidos ########")
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
    print("############ Postres #############")
    print("#1. Frios          #")
    print("#2. Calidos      #")
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
