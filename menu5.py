import libreria

def AgregarAmigos():
    # 1. Pedir nombre
    # 2. Pedir red social
    # 3. Guardadr datos en contactos.txt
    amigo=libreria.pedir_nombre("Ingrese nombre de amigo: ")
    red_s=libreria.pedir_nombre("ingrese red social:")
    contenido = amigo + "-" + red_s + "\n"
    libreria.agregar_datos("amigos.txt", contenido,"a")
    print("se agrego n nuevo amigo")

def MostrarAmigos():
    # 1. Abrir el archivo amigos.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("amigos.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            amigo, red_s= item.split("-")
            msg="{} es un amigo de {}"
            amigo=amigo.replace("\n","")
            red_s=red_s.replace("\n","")
            print(msg.format(amigo, red_s))
        #fin_for
    else:
        print("No hay datos")



opc=""
max=3
while(opc!=max):
    print("######## MENU ###############")
    print("#1. Agregar amigos          #")
    print("#2. Mostrar amigos          #")
    print("#3. Salir                   #")
    print("#############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarAmigos()
    if(opc==2):
        MostrarAmigos()
    #fin if
#fin while
print("fin")
