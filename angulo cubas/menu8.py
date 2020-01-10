import libreria

def agregarCreditos():
    # 1. Pedir la Creditos
    curso=libreria.pedir_nombre("Ingrese el nombre del curso:")
    creditos=libreria.pedir_entero("Ingrese el numero de creditos:")
    # 2. Guardar los creditos  en el archivo creditos.txt
    contenido= curso+ "-" + creditos + "\n"
    libreria.guardar_datos("creditos.txt", contenido, "a")
    print("Datos guardados")

def mostrarCreditos():
    # 1. Abrir el archivo creditos.txt y mostrar sus datos
    data=libreria.obtener_datos_lista("creditos.txt")
    # 2. Comprobar si hay datos
    if ( data != ""):
        for item in data:
            curso,creditos = item.split("-")
            msg="El curso de {} posee {} creditos"
            curso=curso.replace("\n","")
            creditos=creditos.replace("\n","")
            print(msg.format(curso, creditos))
        #fin_for
    else:
        print("No hay datos")

opc=""
max=3
while(opc != max):
    print("######### MENU ########")
    print("# 1. Agregar Creditos    #")
    print("# 2. Mostrar Creditos    #")
    print("# 3. Salir            #")
    print("#######################")
    opc=libreria.pedir_numero("Ingrese Opcion:", 1, 3)

    if ( opc ==1 ):
        agregarCreditos()
    if ( opc ==2 ):
        mostrarCreditos()
#fin_while
