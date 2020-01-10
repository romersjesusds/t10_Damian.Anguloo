import libreria

def AgregarSubOpcionA():
    #1. pedir numero
    numero=libreria.pedir_cel("Ingrese cel : ")
    familia=libreria.pedir_nombre("Ingrese nombre : ")
    # 2. Guardar datos en familia.txt
    contenido = familia + "-" + numero + "\n"
    libreria.agregar_datos("familia.txt", contenido,"a")
    print("datos guardados")

def MostrarSubOpcionA():
    # 1. Abrir el archivo familia.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("familia.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            familia,numero = item.split("-")
            msg="{} -  {}  "
            numero=numero.replace("\n","")
            familia=familia.replace("\n","")
            print(msg.format(familia,numero))
        #fin_for
    else:
        print("No hay datos")

def AgregarSubOpcionB():
    # 1. pedir numero
    numero1 = libreria.pedir_cel("Ingrese cel : ")
    amigos = libreria.pedir_nombre("Ingrese nombre : ")
    # 2. Guardar datos en amigos.txt
    contenido = amigos + "-" + numero1 + "\n"
    libreria.agregar_datos("amigos.txt", contenido, "a")
    print("datos guardados")


def MostrarSubOpcionB():
    # 1. Abrir el archivo amigos.txt y mostrar sus datos
    datos = libreria.obtener_datos_lista("amigos.txt")
    # 2. Comprobar si hay datos
    if (datos != ""):
        for item in datos:
            amigos, numero1 = item.split("-")
            msg = "{} -  {}  "
            numero1 = numero1.replace("\n", "")
            amigos = amigos.replace("\n", "")
            print(msg.format(amigos, numero1))
        # fin_for
    else:
        print("No hay datos")


def OpcionA():
    print("####### Amigos ########")
    print("#1. Agregar numero    #")
    print("#2. mostrar numero    #")
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
    print("####### Familiares ########")
    print("#1. agregar numero        #")
    print("#2. mostrar numero        #")
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
    print("############ Contactos #############")
    print("#1. Amigos          #")
    print("#2. Familiares      #")
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
