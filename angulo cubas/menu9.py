import libreria

def agregarNota():
    # 1. Pedir la nota
    alumno=libreria.pedir_nombre("Ingrese el nombre del alumno:")
    nota=libreria.pedir_nota("Ingrese nota:",0,20)
    # 2. Guardar la nota en el archivo nota.txt
    contenido= alumno+ "-" + nota + "\n"
    libreria.guardar_datos("nota.txt", contenido, "a")
    print("Datos guardados")

def mostrarNota():
    # 1. Abrir el archivo nota.txt y mostrar sus datos
    data=libreria.obtener_datos_lista("nota.txt")
    # 2. COmprobar si hay datos
    if ( data != ""):
        for item in data:
            alumno,nota = item.split("-")
            msg="El alumno {} tiene nota  {}"
            alumno=alumno.replace("\n","")
            nota=nota.replace("\n","")
            print(msg.format(alumno,nota))
        #fin_for
    else:
        print("No hay datos")

opc=""
max=3
while(opc != max):
    print("######### MENU ########")
    print("# 1. Agregar Nota     #")
    print("# 2. Mostrar Nota     #")
    print("# 3. Salir            #")
    print("#######################")
    opc=libreria.pedir_numero("Ingrese Opcion:", 1, 3)

    if ( opc ==1 ):
        agregarNota()
    if ( opc ==2 ):
        mostrarNota()
#fin_while
