import libreria

def AgregarCapital():
    # 1. Pedir capital
    # 2. Pedir pais
    # 3. Guardadr datos en capitales.txt
    capital=libreria.pedir_capital("Ingrese capital: ")
    pais=libreria.pedir_nombre("ingrese pais:")
    contenido = capital + "-" + pais + "\n"
    libreria.agregar_datos("capitales.txt", contenido,"a")
    print("se agrego una nueva capital")

def MostrarCapital():
    # 1. Abrir el archivo capitales.txt y mostrar sus datos
    datos=libreria.obtener_datos_lista("capitales.txt")
    # 2. Comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            capital, pais= item.split("-")
            msg=" {} es la capital de {}"
            capital=capital.replace("\n","")
            pais=pais.replace("\n","")
            print(msg.format(capital, pais))
        #fin_for
    else:
        print("No hay datos")



opc=""
max=3
while(opc!=max):
    print("######## MENU #############")
    print("#1. Agregar Capital  #")
    print("#2. Mostrar Capital #")
    print("#3. Salir                 #")
    print("###########################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)

    if( opc==1):
        AgregarCapital()
    if(opc==2):
        MostrarCapital()
        #fin if
#fin while
print("fin")
