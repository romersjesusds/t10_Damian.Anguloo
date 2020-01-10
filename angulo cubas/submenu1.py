import libreria

def AgregarSubOpcionA():
    #1. pedir falla
    falla=libreria.pedir_cadena("Ingrese el problema: ")
    equipo=libreria.pedir_cadena("Ingrese el equipo : ")
    # 2. Guardar datos en fallas.txt
    contenido = falla + "-" + equipo + "\n"
    libreria.agregar_datos("fallas.txt", contenido,"a")
    print("contraseña guardada")

def MostrarSubOpcionA():
    # 1. Abrir el archivo fallas.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("contraseñas.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            falla,equipo = item.split("-")
            msg="El/LA {} presenta la siguiente falla:  {}"
            falla=falla.replace("\n","")
            equipo=equipo.replace("\n","")
            print(msg.format(falla,equipo))
        #fin_for
    else:
        print("No hay datos")

def AgregarSubOpcionB():
    #1. pedir lenguaje
    lenguaje=libreria.pedir_nombre("Ingrese lenguaje de programacion: ")
    app=libreria.pedir_app("Ingrese el tipo de aplicacion tipo de aplicacion(game,web,escritorio): ")
    # 2. Guardar datos en lenguaje.txt
    contenido = lenguaje + "-" + app + "\n"
    libreria.agregar_datos("lenguaje.txt", contenido,"a")
    print("Datos guardados")


def MostrarSubOpcionB():
     # 1. Abrir el archivo lenguaje.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("lenguaje.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            lenguaje,app = item.split("-")
            msg=" Se utilizo el lenguaje {} para elaborar una app de tipo:  {}"
            lenguaje=lenguaje.replace("\n","")
            app=app.replace("\n","")
            print(msg.format(lenguaje,app))
        #fin_for
    else:
        print("No hay datos")



def OpcionA():
    print("##### Mantenimiento ########")
    print("#1. Agregar falla     #")
    print("#2. mostrar falla     #")
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
    print("##### Desarrollo ########")
    print("#1. agregar lenguaje     #")
    print("#2. mostrar lenguaje       #")
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
    print("#1. Mantenimiento             #")
    print("#2. Desarrollo                #")
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
