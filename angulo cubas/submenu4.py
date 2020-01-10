import libreria

def AgregarSubOpcionA():
    #1. pedir nota
    nota=libreria.pedir_nota("Ingrese nota : ",0,20)
    alumno=libreria.pedir_nombre("Ingrese alumno : ")
    # 2. Guardar datos en mate.txt
    contenido = alumno + "-" + nota + "\n"
    libreria.agregar_datos("mate.txt", contenido,"a")
    print("datos guardados")

def MostrarSubOpcionA():
    # 1. Abrir el archivo mate.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("mate.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            nota,alumno = item.split("-")
            msg="El alumno {} presenta  {} de promedio en matematicas "
            nota=nota.replace("\n","")
            alumno=alumno.replace("\n","")
            print(msg.format(alumno,nota))
        #fin_for
    else:
        print("No hay datos")

def AgregarSubOpcionB():
    #1. pedir carrera
    nota1=libreria.pedir_nota("Ingrese nota: ")
    alumno1=libreria.pedir_nombre("Ingrese alumno: ")
    # 2. Guardar datos en histo.txt
    contenido = nota1 + "-" + alumno1 + "\n"
    libreria.agregar_datos("doctor.txt", contenido,"a")
    print("Datos guardados")


def MostrarSubOpcionB():
     # 1. Abrir el archivo histo.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("histo.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            nota1,alumno1 = item.split("-")
            msg="El alumno {} presenta  {} de promedio en historia "
            nota1=nota1.replace("\n","")
            alumno1=alumno1.replace("\n","")
            print(msg.format(alumno1,nota1))
        #fin_for
    else:
        print("No hay datos")



def OpcionA():
    print("##### Matematicas ########")
    print("#1. Agregar nota     #")
    print("#2. mostrar nota     #")
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
    print("##### Historia ########")
    print("#1. agregar nota     #")
    print("#2. mostrar nota       #")
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
    print("############ Cursos #############")
    print("#1. Matematicas          #")
    print("#2. Historia                #")
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
