import libreria

def AgregarSubOpcionA():
    #1. pedir madera
    madera=libreria.pedir_cadena("Ingrese el tipo de madera: ")
    precio=libreria.pedir_precio("Ingrese precio : ",100,1000)
    # 2. Guardar datos en armario.txt
    contenido = madera + "-" + precio + "\n"
    libreria.agregar_datos("armario.txt", contenido,"a")
    print("datos guardados")

def MostrarSubOpcionA():
    # 1. Abrir el archivo armario.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("armario.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            madera,precio = item.split("-")
            msg="El armario de madera  {} cuesta  {} soles  "
            madera=madera.replace("\n","")
            precio=precio.replace("\n","")
            print(msg.format(madera,precio))
        #fin_for
    else:
        print("No hay datos")

def AgregarSubOpcionB():
    # 1. pedir madera
    madera1 = libreria.pedir_cadena("Ingrese el tipo de madera: ")
    precio1 = libreria.pedir_precio_mueble("Ingrese precio : ")
    # 2. Guardar datos en mesa.txt
    contenido = madera1 + "-" + precio1 + "\n"
    libreria.agregar_datos("mesa.txt", contenido, "a")
    print("datos guardados")


def MostrarSubOpcionB():
    # 1. Abrir el archivo mesa.txt y mostrar sus datos
    datos = libreria.obtener_datos_lista("mesa.txt")
    # 2. Comprobar si hay datos
    if (datos != ""):
        for item in datos:
            madera, precio = item.split("-")
            msg = "La mesa de madera  {} cuesta  {} soles  "
            madera1 = madera1.replace("\n", "")
            precio1 = precio1.replace("\n", "")
            print(msg.format(madera1, precio1))
        # fin_for
    else:
        print("No hay datos")


def OpcionA():
    print("####### Mesas ########")
    print("#1. agregar madera    #")
    print("#2. mostrar madera    #")
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
    print("####### Armarios ########")
    print("#1. agregar madera      #")
    print("#2. mostrar madera      #")
    print("#3. salir               #")
    print("#########################")
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
    print("###### Muebles de Madera ######")
    print("#1. Mesas            #")
    print("#2. Armarios         #")
    print("#3. Salir            #")
    print("#####################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        OpcionA()
    if(opc==2):
        OpcionB()
    #fin if
#fin while
print("fin")
