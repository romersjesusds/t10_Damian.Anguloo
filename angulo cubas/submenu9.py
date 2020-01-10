import libreria

def AgregarSubOpcionA():
    #1. pedir patologia
    patologia=libreria.pedir_cadena("Ingrese enfermedad : ")
    paciente=libreria.pedir_nombre("Ingrese nombre : ")
    # 2. Guardar datos en derma.txt
    contenido = paciente + "-" + patologia + "\n"
    libreria.agregar_datos("derma.txt", contenido,"a")
    print("datos guardados")

def MostrarSubOpcionA():
    # 1. Abrir el archivo derma.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("derma.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            paciente,patologia = item.split("-")
            msg="El paciente  {} padece de  {}  "
            patologia=patologia.replace("\n","")
            paciente=paciente.replace("\n","")
            print(msg.format(paciente,patologia))
        #fin_for
    else:
        print("No hay datos")

def AgregarSubOpcionB():
    # 1. pedir patologia
    patologia1 = libreria.pedir_cadena("Ingrese enfermedad : ")
    paciente1 = libreria.pedir_nombre("Ingrese nombre : ")
    # 2. Guardar datos en psico.txt
    contenido = paciente1 + "-" + patologia1 + "\n"
    libreria.agregar_datos("psico.txt", contenido, "a")
    print("datos guardados")


def MostrarSubOpcionB():
    # 1. Abrir el archivo psico.txt y mostrar sus datos
    datos = libreria.obtener_datos_lista("psico.txt")
    # 2. Comprobar si hay datos
    if (datos != ""):
        for item in datos:
            paciente1, patologia1 = item.split("-")
            msg = "El paciente  {} padece de  {}  "
            patologia1 = patologia1.replace("\n", "")
            paciente1 = paciente1.replace("\n", "")
            print(msg.format(paciente1, patologia1))
        # fin_for
    else:
        print("No hay datos")


def OpcionA():
    print("####### Dermatologia ########")
    print("#1. agregar patologia    #")
    print("#2. mostrar patologia    #")
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
    print("####### Psiquiatria ########")
    print("#1. agregar patologia        #")
    print("#2. mostrar patologia        #")
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
    print("###### Medicina ######")
    print("#1. Dermatologia       #")
    print("#2. Psiquiatria         #")
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
