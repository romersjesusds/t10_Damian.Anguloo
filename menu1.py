import libreria

def AgregarRaza():
    # 1. Pedir raza
    # 2. Pedir animal
    # 3. Guardadr datos en razas.txt
    raza=libreria.pedir_nombre("Ingrese raza: ")
    animal=libreria.pedir_nombre("ingrese animal:")
    contenido = raza + "-" + animal + "\n"
    libreria.agregar_datos("razas.txt", contenido,"a")
    print("se agrego una nueva raza ")

def MostrarRazas():
    # 1. Abrir el archivo razas.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("razas.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            raza, animal= item.split("-")
            msg="'{}' es raza de {}"
            raza=raza.replace("\n","")
            animal=animal.replace("\n","")
            print(msg.format(raza, animal))
        #fin_for
    else:
        print("sin datos")



opc=""
max=3
while(opc!=max):
    print("############ MENU #############")
    print("#1. Agregar razas de animales #")
    print("#2. Mostrar razas             #")
    print("#3. Salir                     #")
    print("###############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarRaza()
    if(opc==2):
        MostrarRazas()
    #fin if
#fin while
print("fin")
