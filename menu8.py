import libreria

def AgregarCodigo():
    # 1. Pedir codigo
    # 2. Pedir nombre
    # 3. Guardadr datos en codigos_student.txt
    codigo=libreria.pedir_codigo("Ingrese codigo: ")
    nombre=libreria.pedir_nombre("ingrese nombre:")
    contenido = str(codigo) + "-" + nombre + "\n"
    libreria.agregar_datos("codigos_student.txt", contenido,"a")
    print("se agrego un nuevo codigo de estudiante")

def MostrarCodigos():
    # 1. Abrir el archivo codigos_student.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("codigos_student.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            codigo, nombre= item.split("-")
            msg="{} es el codigo del estudiante -> {}"
            codigo=codigo.replace("\n","")
            nombre=nombre.replace("\n","")
            print(msg.format(codigo, nombre))
        #fin_for
    else:
        print("No hay datos")



opc=""
max=3
while(opc!=max):
    print("############### MENU ###############")
    print("#1. Agregar codigo de estudiante   #")
    print("#2. Mostrar codigos                #")
    print("#3. Salir                          #")
    print("####################################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarCodigo()
    if(opc==2):
        MostrarCodigos()
    #fin if
#fin while
print("fin")
