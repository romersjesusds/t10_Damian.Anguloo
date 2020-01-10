import libreria

def AgregarContacto():
    # 1. Pedir numero de telefono
    # 2. Pedir nombre
    # 3. Guardadr datos en contactos.txt
    telefono=libreria.pedir_telefono("Ingrese numero de telefono: ")
    nombre=libreria.pedir_nombre("ingrese nombre:")
    contenido = telefono + "-" + nombre + "\n"
    libreria.agregar_datos("contactos.txt", contenido,"a")
    print("se agrego un nuevo contacto")

def MostrarContactos():
    # 1. Abrir el archivo contactos.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("contactos.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            telefono, nombre= item.split("-")
            msg="{} es el telefono de {}"
            telefono=telefono.replace("\n","")
            nombre=nombre.replace("\n","")
            print(msg.format(telefono, nombre))
        #fin_for
    else:
        print("No hay datos")



opc=""
max=3
while(opc!=max):
    print("######## MENU ###############")
    print("#1. Agregar nuevo contacto  #")
    print("#2. Mostrar contactos       #")
    print("#3. Salir                   #")
    print("#############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarContacto()
    if(opc==2):
        MostrarContactos()
    #fin if
#fin while
print("fin")
