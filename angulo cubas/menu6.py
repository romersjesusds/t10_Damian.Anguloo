import libreria

def agregarPlaca():
    # 1. Pedir la placa
    dueño=libreria.pedir_nombre("Ingrese el nombre del dueño:")
    placa=libreria.pedir_placa("Ingrese el numero de placa:")
    # 2. Guardar la placa en el archivo placa.txt
    contenido= dueño+ "-" + placa + "\n"
    libreria.guardar_datos("placa.txt", contenido, "a")
    print("Datos guardados")

def mostrarPlaca():
    # 1. Abrir el archivo placa.txt y mostrar sus datos
    data=libreria.obtener_datos_lista("placa.txt")
    # 2. Comprobar si hay datos
    if ( data != ""):
        for item in data:
            nombre,placa = item.split("-")
            msg="El auto de placa {} es propiedad de {}"
            dueño=dueño.replace("\n","")
            placa=placa.replace("\n","")
            print(msg.format(dueño, placa))
        #fin_for
    else:
        print("No hay datos")

opc=""
max=3
while(opc != max):
    print("######### MENU ########")
    print("# 1. Agregar Placa    #")
    print("# 2. Mostrar Placa    #")
    print("# 3. Salir            #")
    print("#######################")
    opc=libreria.pedir_numero("Ingrese Opcion:", 1, 3)

    if ( opc ==1 ):
        agregarPlaca()
    if ( opc ==2 ):
        mostrarPlaca()
#fin_while
