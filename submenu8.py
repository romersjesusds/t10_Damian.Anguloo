import libreria

def AgregarSubOpcionA():
    #1. pedir carrera
    #2. Guardadr datos en carreras.txt
    carreras=libreria.pedir_nombre("Ingrese carrera: ")
    facultad=libreria.pedir_nombre("Ingrese facultad: ")
    contenido = carreras + "-" + facultad + "\n"
    libreria.agregar_datos("carreras.txt", contenido,"a")
    print("carrera nueva agregada")

def MostrarSubOpcionA():
    # 1. Abrir el archivo carreras.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("carreras.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            carreras, facultad= item.split("-")
            msg="'{}' pertenece a la facultad de {}"
            carreras=carreras.replace("\n","")
            facultad=facultad.replace("\n","")
            print(msg.format(carreras, facultad))
        #fin_for
    else:
        print("No hay datos")

def AgregarSubOpcionB():
    #1. pedir carrera
    #2. Guardadr datos en carreras.txt
    carreras=libreria.pedir_nombre("Ingrese carrera: ")
    facultad=libreria.pedir_nombre("Ingrese facultad: ")
    contenido = carreras + "-" + facultad + "\n"
    libreria.agregar_datos("carreras.txt", contenido,"a")
    print("carrera nueva agregada")


def MostrarSubOpcionB():
    # 1. Abrir el archivo carreras.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("carreras.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            carreras, facultad= item.split("-")
            msg="'{}' pertenece a la facultad de {}"
            carreras=carreras.replace("\n","")
            facultad=facultad.replace("\n","")
            print(msg.format(carreras, facultad))
        #fin_for
    else:
        print("No hay datos")



def OpcionA():
    print("##### CARRERAS-NUMEROS ########")
    print("#1. Agregar  CARRERAS         #")
    print("#2. mostrar CARRERAS          #")
    print("#3. salir                     #")
    print("###############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarSubOpcionA()
    if(opc==2):
        MostrarSubOpcionB()
    #fin if
#fin while

def OpcionB():
    print("##### CARRERAS-LETRAS ########")
    print("#1. agregar CARRERAS         #")
    print("#2. mostrar CARRERAS         #")
    print("#3. salir                    #")
    print("##############################")
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
    print("################# MENU ###############")
    print("#1. carreras que llevan mas numeros  #")
    print("#2. carreras que llevan mas letras   #")
    print("#3. Salir                            #")
    print("######################################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        OpcionA()
    if(opc==2):
        OpcionB()
    #fin if
#fin while
print("fin")

