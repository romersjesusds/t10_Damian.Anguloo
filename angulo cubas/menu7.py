import libreria

def agregarClub():
    # 1. Pedir club
    pais=libreria.pedir_nombre("Ingrese el nombre del pais:")
    club=libreria.pedir_nombre("Ingrese el nombre del club:")
    # 2. Guardar el club en el archivo club.txt
    contenido= pais+ "-" + club + "\n"
    libreria.guardar_datos("club.txt", contenido, "a")
    print("Datos guardados")

def mostrarClub():
    # 1. Abrir el archivo club.txt y mostrar sus datos
    data=libreria.obtener_datos_lista("club.txt")
    # 2. Comprobar si hay datos
    if ( data != ""):
        for item in data:
            pais,club = item.split("-")
            msg=" {} es un equipo de {}"
            pais=pais.replace("\n","")
            club=club.replace("\n","")
            print(msg.format(pais, club))
        #fin_for
    else:
        print("No hay datos")

opc=""
max=3
while(opc != max):
    print("######### MENU ########")
    print("# 1. Agregar Club     #")
    print("# 2. Mostrar Club     #")
    print("# 3. Salir            #")
    print("#######################")
    opc=libreria.pedir_numero("Ingrese Opcion:", 1, 3)

    if ( opc ==1 ):
        agregarClub()
    if ( opc ==2 ):
        mostrarClub()
#fin_while
