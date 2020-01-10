import libreria

def AgregarSubOpcionA():
    #1. pedir carrera
    carrera=libreria.pedir_cadena("Ingrese  carrera de ingenieria: ")
    tiempo=libreria.pedir_tiempo_estudio("Ingrese el tiempo : ",5,10)
    # 2. Guardar datos en inge.txt
    contenido = carrera + "-" + tiempo + "años" + "\n"
    libreria.agregar_datos("inge.txt", contenido,"a")
    print("Datos guardados")

def MostrarSubOpcionA():
    # 1. Abrir el archivo inge.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("inge.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            carrera,tiempo = item.split("-")
            msg="La  carrera de{} dura {} años"
            carrera=carrera.replace("\n","")
            tiempo=tiempo.replace("\n","")
            print(msg.format(carrera,tiempo))
        #fin_for
    else:
        print("No hay datos")

def AgregarSubOpcionB():
    #1. pedir carrera
    carrera1=libreria.pedir_cadena("Ingrese carrera de comuniaciones: ")
    tiempo1=libreria.pedir_tiempo("Ingrese tiempo: ")
    # 2. Guardar datos en comu.txt
    contenido = carrera1 + "-" + tiempo1 + "años" + "\n"
    libreria.agregar_datos("comu.txt", contenido,"a")
    print("Datos guardados")


def MostrarSubOpcionB():
     # 1. Abrir el archivo comu.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("comu.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            lenguaje,app = item.split("-")
            msg="La  carrera de{} dura {} años"
            carrera1=carrera1.replace("\n","")
            tiempo1=tiempo1.replace("\n","")
            print(msg.format(carrera1,tiempo1))
        #fin_for
    else:
        print("No hay datos")



def OpcionA():
    print("##### Ingenierias ########")
    print("#1. Agregar carrera     #")
    print("#2. mostrar carrera     #")
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
    print("##### Comunicaciones ########")
    print("#1. agregar carrera     #")
    print("#2. mostrar carrera       #")
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
    print("############ Pregrado #############")
    print("#1. Ingenierias           #")
    print("#2. Comunicaciones                #")
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
