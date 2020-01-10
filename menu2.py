import libreria

def AgregarDistritos():
    # 1. Pedir distrito
    # 2. Pedir departamento
    # 3. pedir Pais
    # 4. Guardadr datos en distritos.txt
    distrito=libreria.pedir_lugar("Ingrese distrito: ")
    departamento=libreria.pedir_lugar("ingrese departamento:")
    pais=libreria.pedir_lugar("Ingrese Pais:")
    contenido = distrito + "-" + departamento + "-" + pais + "\n"
    libreria.agregar_datos("distritos.txt", contenido,"a")
    print("se agrego un nuevo distrito")

def MostrarDistritos():
    # 1. Abrir el archivo distritos.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("distritos.txt")
    # 2. COmprobar si hay datos
    if ( datos != ""):
        for item in datos:
            distrito, departamento, pais = item.split("-")
            msg="el distrito {} pertenece al departameto de {} en {}"
            distrito=distrito.replace("\n","")
            departamento=departamento.replace("\n","")
            pais=pais.replace("\n","")
            print(msg.format(distrito, departamento, pais))
        #fin_for
    else:
        print("No hay datos")




opc=""
max=3
while(opc!=max):
    print("############### MENU ##################")
    print("#1. Agregar distritos                 #")
    print("#2. Mostrar distritos                 #")
    print("#3. Salir                             #")
    print("#######################################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarDistritos()
    if(opc==2):
        MostrarDistritos()
    #fin if
#fin while
