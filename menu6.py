import libreria

def AgregarPlato():
    # 1. Pedir Plato
    # 2. Pedir lugar de procedencia
    # 3. Guardar datos en platos_tipicos.txt
    plato=libreria.pedir_nombre("Ingrese plato tipico: ")
    lugar=libreria.pedir_lugar("ingrese lugar-procedencia:")
    region=libreria.pedir_lugar("ingrese region:")
    contenido = plato + "-" + lugar + "-" + region + "\n"
    libreria.agregar_datos("platos_tipicos.txt", contenido,"a")
    print("se agrego un nuevo plato tipico")

def MostrarPlato():
    # 1. Abrir el archivo platos_tipicos.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("platos_tipicos.txt")
    # 2. COmprobar si hay datos
    if ( datos != ""):
        for item in datos:
            plato, lugar, region= item.split("-")
            msg="El/la {} es un plato tipico de {} - {}"
            plato=plato.replace("\n","")
            lugar=lugar.replace("\n","")
            region=region.replace("\n","")
            print(msg.format(plato, lugar, region))
        #fin_for
    else:
        print("No hay datos")



opc=""
max=3
while(opc!=max):
    print("######## MENU ###############")
    print("#1. Agregar platos tipicos  #")
    print("#2. Mostrar platos ticos    #")
    print("#3. Salir                   #")
    print("#############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarPlato()
    if(opc==2):
        MostrarPlato()
    #fin if
#fin while
print("fin")
