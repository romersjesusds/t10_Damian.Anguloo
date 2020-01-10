import libreria

def AgregarPromedio():
    # 1. Pedir curso
    # 2. Pedir promedio
    # 3. Guardadr datos en promedios.txt
    curso=libreria.pedir_nombre("Ingrese nombre: ")
    promedio=libreria.pedir_real("ingrese promedio:")
    contenido = curso + "-" + str(promedio) + "\n"
    libreria.agregar_datos("promedios.txt", contenido,"a")
    print("se agrego un nuevo promedio")

def MostrarPromedios():
    # 1. Abrir el archivo promedios.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("promedios.txt")
    # 2. COmprobar si hay datos
    if ( datos != ""):
        for item in datos:
            curso, promedio= item.split("-")
            msg="En el curso de {} tienes de promedio {}"
            curso=curso.replace("\n","")
            promedio=promedio.replace("\n","")
            print(msg.format(curso, promedio))
        #fin_for
    else:
        print("No hay datos")



opc=""
max=3
while(opc!=max):
    print("############### MENU ################")
    print("#1. Agregar promedio de un curso    #")
    print("#2. Mostrar promedios               #")
    print("#3. Salir                           #")
    print("#####################################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarPromedio()
    if(opc==2):
        MostrarPromedios()
    #fin if
#fin while
print("fin")
