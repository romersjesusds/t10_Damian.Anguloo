import libreria

def AgregarObra():
    # 1. Pedir nombre de la obra
    # 2. Pedir nombre del autor
    # 3. pedir año de publicacion
    # 4. Guardadr datos en obras.txt
    obra=libreria.pedir_nombre("Ingrese obra: ")
    autor=libreria.pedir_nombre("ingrese nombre del autor:")
    anio_publ=libreria.pedir_entero("ingrese año de publicacion:")
    contenido = obra + "-" + autor + "-" + str(anio_publ) + "\n"
    libreria.agregar_datos("obras.txt", contenido,"a")
    print("se agrego una nueva obra literaria")

def MostrarObras():
    # 1. Abrir el archivo obras.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("obras.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            obra, autor, anio_publ= item.split("-")
            msg="el autor de '{}' es {} y la obra fue publicada el año {}"
            obra=obra.replace("\n","")
            autor=autor.replace("\n","")
            anio_publ=anio_publ.replace("\n","")
            print(msg.format(obra, autor, anio_publ))
        #fin_for
    else:
        print("No hay datos")



opc=""
max=3
while(opc!=max):
    print("############# MENU ##############")
    print("#1. Agregar obras de literatura #")
    print("#2. Mostrar obras de literatura #")
    print("#3. Salir                       #")
    print("#################################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarObra()
    if(opc==2):
        MostrarObras()
    #fin if
#fin while
print("fin")
