import libreria

def AgregarSubOpcionA():
    #1. pedir area
    area=libreria.pedir_cadena("Ingrese area de investigacion : ")
    uni=libreria.pedir_nombre("Ingrese la universidad : ")
    # 2. Guardar datos en maestria.txt
    contenido = area + "-" + uni + "\n"
    libreria.agregar_datos("maestria.txt", contenido,"a")
    print("Datos guardados")

def MostrarSubOpcionA():
    # 1. Abrir el archivo maestria.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("maestria.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            area,uni = item.split("-")
            msg="Maestria en el area de {} en la universidad {} "
            area=area.replace("\n","")
            uni=uni.replace("\n","")
            print(msg.format(area,uni))
        #fin_for
    else:
        print("No hay datos")

def AgregarSubOpcionB():
    #1. pedir carrera
    area1=libreria.pedir_cadena("Ingrese el area de investigacion: ")
    uni1=libreria.pedir_nombre("Ingrese universidad: ")
    # 2. Guardar datos en doctor.txt
    contenido = area1 + "-" + uni1 + "\n"
    libreria.agregar_datos("doctor.txt", contenido,"a")
    print("Datos guardados")


def MostrarSubOpcionB():
     # 1. Abrir el archivo doctor.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("doctor.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            area1,uni1 = item.split("-")
            msg="Doctorado en el area de {} en la universidad {} "
            area1=area1.replace("\n","")
            uni1=uni1.replace("\n","")
            print(msg.format(area1,uni1))
        #fin_for
    else:
        print("No hay datos")



def OpcionA():
    print("##### Maestria ########")
    print("#1. Agregar area     #")
    print("#2. mostrar area     #")
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
    print("##### Doctorado ########")
    print("#1. agregar area     #")
    print("#2. mostrar area       #")
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
    print("############ Posgrado #############")
    print("#1. Maestria           #")
    print("#2. Doctorado                #")
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
