import libreria

def AgregarSubOpcionA():
    #1. pedir TELEFONO
    #2. Guardadr datos en Llamdas.txt
    telefono=libreria.pedir_telefono("Ingrese nro de telefono: ")
    codigo_pais=libreria.pedir_cadena("Ingrese codigo: ")
    contenido = codigo_pais + "-" + telefono + "\n"
    libreria.agregar_datos("llamadas.txt", contenido,"a")
    print("llamada nueva guardada")
    print("llamando...")


def MostrarSubOpcionA():
    # 1. Abrir el archivo llamadas.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("llamadas.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            codigo_pais, telefono = item.split("-")
            msg="{} {} se llamó a este numero"
            codigo_pais=codigo_pais.replace("\n","")
            telefono=telefono.replace("\n","")
            print(msg.format(codigo_pais, telefono))
        #fin_for
    else:
        print("No hay datos")

def AgregarSubOpcionB():
    #1. pedir mensaje
    #2. Guardadr datos en mensajes.txt
    mensaje=libreria.pedir_cadena("Ingrese mensaje: ")
    telefono=libreria.pedir_telefono("Ingrese nro de telefono_destino: ")
    contenido = mensaje + "-" + telefono + "\n"
    libreria.agregar_datos("mensajes.txt", contenido,"a")
    print("mensaje nuevo guardado con exito")
    print("enviando mensaje...")


def MostrarSubOpcionB():
     # 1. Abrir el archivo mensajes.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("mensajes.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            mensaje, nro_telefono = item.split("-")
            msg="el mensaje '{}' se envio al numero {}"
            mensaje=mensaje.replace("\n","")
            nro_telefono=nro_telefono.replace("\n","")
            print(msg.format(mensaje, nro_telefono))
        #fin_for
    else:
        print("No hay datos")



def OpcionA():
    print("######### LLAMADA ########")
    print("#1. Agregar  LLAMADA     #")
    print("#2. mostrar LLAMADAS     #")
    print("#3. salir                #")
    print("##########################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarSubOpcionA()
    if(opc==2):
        MostrarSubOpcionA()
    #fin if
#fin while

def OpcionB():
    print("######### MENSAJE ########")
    print("#1. agregar MENSAJE      #")
    print("#2. mostrar MENSAJE      #")
    print("#3. salir                #")
    print("##########################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarSubOpcionB()
    if(opc==2):
        MostrarSubOpcionB()
    #fin if
#fin while

opc=""
max=3
while(opc!=max):
    print("############ MENU #############")
    print("#1. Llamada                   #")
    print("#2. Mensaje                   #")
    print("#3. Salir                     #")
    print("###############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        OpcionA()
    if(opc==2):
        OpcionB()
    #fin if
#fin while
print("fin")
