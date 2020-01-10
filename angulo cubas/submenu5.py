import libreria

def AgregarSubOpcionA():
    #1. pedir pelicula
    pelicula=libreria.pedir_cadena("Ingrese  pelicula: ")
    cine=libreria.pedir_nombre("Ingrese cine : ")
    precio = libreria.pedir_precio("Ingrese precio : ",5,20)
    # 2. Guardar datos en terror.txt
    contenido = pelicula + "-" + cine + precio + "\n"
    libreria.agregar_datos("terror.txt", contenido,"a")
    print("Datos guardados")

def MostrarSubOpcionA():
    # 1. Abrir el archivo terror.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("terror.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            pelicula,cine,precio = item.split("-")
            msg="La  pelicula de {} cuesta {} soles, en {}"
            pelicula=pelicula.replace("\n","")
            cine=cine.replace("\n","")
            precio=precio.replace("\n", "")
            print(msg.format(pelicula,precio,cine))
        #fin_for
    else:
        print("No hay datos")

def AgregarSubOpcionB():
    # 1. pedir pelicula
    pelicula1 = libreria.pedir_cadena("Ingrese  pelicula: ")
    cine1 = libreria.pedir_nombre("Ingrese cine : ")
    precio1 = libreria.pedir_precio_cine("Ingrese precio : ")
    # 2. Guardar datos en comedia.txt
    contenido = pelicula1 + "-" + cine1 + precio1 + "\n"
    libreria.agregar_datos("terror.txt", contenido, "a")
    print("Datos guardados")


def MostrarSubOpcionB():
    # 1. Abrir el archivo comedia.txt y mostrar sus datos
    datos = libreria.obtener_datos_lista("comedia.txt")
    # 2. Comprobar si hay datos
    if (datos != ""):
        for item in datos:
            pelicula1, cine1, precio1 = item.split("-")
            msg = "La  pelicula de {} cuesta {} soles, en {}"
            pelicula1 = pelicula1.replace("\n", "")
            cine1 = cine1.replace("\n", "")
            precio1 = precio1.replace("\n", "")
            print(msg.format(pelicula1, precio1, cine1))
        # fin_for
    else:
        print("No hay datos")


def OpcionA():
    print("##### Terror ########")
    print("#1. Agregar pelicula     #")
    print("#2. mostrar pelicula     #")
    print("#3. salir             #")
    print("#############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarSubOpcionA()
    if(opc==2):
        MostrarSubOpcionA()
    #fin if
#fin while

def OpcionB():
    print("##### Comedia ########")
    print("#1. agregar pelicula     #")
    print("#2. mostrar pelicula       #")
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
    print("############ Cine #############")
    print("#1. Terror           #")
    print("#2. Comedia                #")
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
