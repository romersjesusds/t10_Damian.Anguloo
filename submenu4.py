import libreria

def AgregarSubOpcionA():
    #1. pedir comentario
    #2. Guardadr datos en comentarios.txt
    comentario=libreria.pedir_cadena("Ingrese comentario: ")
    duenio_foto=libreria.pedir_nombre("Ingrese nombre: ")
    contenido = comentario + "-" + duenio_foto + "\n"
    libreria.agregar_datos("comentarios.txt", contenido,"a")
    print("se guardó un nuevo comentario")
    print("comentaste la foto")

def MostrarSubOpcionA():
    # 1. Abrir el archivo comentarios.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("comentarios.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            comentario, duenio_foto = item.split("-")
            msg="comentaste '{}' a la foto de {}"
            comentario=comentario.replace("\n","")
            duenio_foto=duenio_foto.replace("\n","")
            print(msg.format(comentario, duenio_foto))
        #fin_for
    else:
        print("No hay datos")

def AgregarSubOpcionB():
    #1. pedir reaccion
    #2. Guardadr datos en reaccion.txt
    reacion=libreria.pedir_nombre("Ingrese reccion: ")
    duenio_foto=libreria.pedir_nombre("Ingrese nombre: ")
    contenido = reacion + "-" + duenio_foto + "\n"
    libreria.agregar_datos("reaccion.txt", contenido,"a")
    print("nueva reaccion guardada")
    print("reaccionaste a una foto")


def MostrarSubOpcionB():
     # 1. Abrir el archivo reaccion.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("reaccion.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            reaccion, duenio_foto= item.split("-")
            msg="le diste '{}' a la foto de {}"
            reaccion=reaccion.replace("\n","")
            duenio_foto=duenio_foto.replace("\n","")
            print(msg.format(reaccion, duenio_foto))
        #fin_for
    else:
        print("No hay datos")



def OpcionA():
    print("##### COMENTAR FOTO ########")
    print("#1. Agregar COMENTARIO     #")
    print("#2. Mostrar COMENTARIO     #")
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
    print("##### REACCIONAR A FOTO ########")
    print("#1. AGREGAR REACCION           #")
    print("#2. MOSTRAR REACCIONES         #")
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
    print("#1. COMENTAR FOTO           #")
    print("#2. REACIONAR A FOTO             #")
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
