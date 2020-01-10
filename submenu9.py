import libreria

def AgregarSubOpcionA():
    #1. pedir musica
    #2. Guardadr datos en musica.txt
    musica=libreria.pedir_cadena("Ingrese musica: ")
    autor=libreria.pedir_nombre("Ingrese autor: ")
    contenido = musica + "-" + autor + "\n"
    libreria.agregar_datos("musica.txt", contenido,"a")
    print("se agrego una nueva musica ")


def MostrarSubOpcionA():
    # 1. Abrir el archivo musica.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("musica.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            musica, autor = item.split("-")
            msg="la musica '{}' pertenece al autor {}"
            musica=musica.replace("\n","")
            autor=autor.replace("\n","")
            print(msg.format(musica, autor))
        #fin_for
    else:
        print("No hay datos")

def AgregarSubOpcionB():
    video=libreria.pedir_cadena("Ingrese video: ")
    autor=libreria.pedir_nombre("Ingrese autor: ")
    contenido = video + "-" + autor + "\n"
    libreria.agregar_datos("video.txt", contenido,"a")
    print("se agrego un nuevo video ")

def MostrarSubOpcionB():
    # 1. Abrir el archivo video.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("video.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            video, autor = item.split("-")
            msg="el video '{}' pertenece al autor {}"
            video=video.replace("\n","")
            autor=autor.replace("\n","")
            print(msg.format(video, autor))
        #fin_for
    else:
        print("No hay datos")




def OpcionA():
    print("######### MUSICA ########")
    print("#1. Agregar MUSICA      #")
    print("#2. mostrar MUSICA      #")
    print("#3. salir                #")
    print("##########################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarSubOpcionA()
    if(opc==2):
        MostrarSubOpcionA()
    #fin if
#fin while

def OpcionB():
    print("######### VIDEO ########")
    print("#1. agregar VIDEO      #")
    print("#2. mostrar VIDEOS     #")
    print("#3. salir              #")
    print("########################")
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
    print("#1. musica (mp3)              #")
    print("#2. video                     #")
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
