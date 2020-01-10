import libreria

def agregarRUC():
    # 1. Pedir el direccion
    empresa=libreria.pedir_nombre("Ingrese el nombre de la empresa:")
    RUC=libreria.pedir_ruc("Ingrese el RUC:")
    # 2. Guardar la direccion en el archivo direc.txt
    contenido= empresa+ "-" + RUC + "\n"
    libreria.guardar_datos("ruc.txt", contenido, "a")
    print("Datos guardados")

def mostrarRUC():
    # 1. Abrir el archivo ruc.txt y mostrar sus datos
    data=libreria.obtener_datos_lista("ruc.txt")
    # 2. COmprobar si hay datos
    if ( data != ""):
        for item in data:
            empresa, RUC = item.split("-")
            msg="La empresa {} con RUC {}"
            empresa=empresa.replace("\n","")
            RUC=RUC.replace("\n","")
            print(msg.format(empresa, RUC))
        #fin_for
    else:
        print("No hay datos")

opc=""
max=3
while(opc != max):
    print("######### MENU ########")
    print("# 1. Agregar RUC      #")
    print("# 2. Mostrar RUC      #")
    print("# 3. Salir            #")
    print("#######################")
    opc=libreria.pedir_numero("Ingrese Opcion:", 1, 3)

    if ( opc ==1 ):
        agregarRUC()
    if ( opc ==2 ):
        mostrarRUC()
#fin_while
