import libreria

def agregarSexo():
    # 1. Pedir el Codigo
    nombre=libreria.pedir_nombre("Ingrese la nombre:")
    sexo=libreria.pedir_sexo("Ingrese el sexo:")
    # 2. Guardar la direccion en el archivo sexo.txt
    contenido= nombre+ "-" + sexo + "\n"
    libreria.guardar_datos("sexo.txt", contenido, "a")
    print("Datos guardados")

def mostrarSexo():
    # 1. Abrir el archivo sexo.txt y mostrar sus datos
    data=libreria.obtener_datos_lista("sexo.txt")
    # 2. COmprobar si hay datos
    if ( data != ""):
        for item in data:
            nombre, sexo = item.split("-")
            msg=" {} es de sexo {}"
            nombre=nombre.replace("\n","")
            sexo=sexo.replace("\n","")
            print(msg.format(nombre,sexo))
        #fin_for
    else:
        print("No hay datos")

opc=""
max=3
while(opc != max):
    print("######### MENU ########")
    print("# 1. Agregar Sexo     #")
    print("# 2. Mostrar Sexo     #")
    print("# 3. Salir            #")
    print("#######################")
    opc=libreria.pedir_numero("Ingrese Opcion:", 1, 3)

    if ( opc ==1 ):
        agregarSexo()
    if ( opc ==2 ):
        mostrarSexo()
#fin_while
