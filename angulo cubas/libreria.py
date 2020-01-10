def guardar_datos(nombre_archivo, contenido, modo):
    archivo=open(nombre_archivo, modo)
    archivo.write(contenido)
    archivo.close()

def obtener_datos(nombre_archivo):
    archivo=open(nombre_archivo)
    contenido = archivo.read()
    archivo.close()
    return contenido

def obtener_datos_lista(nombre_archivo):
    archivo=open(nombre_archivo)
    lista = archivo.readlines()
    archivo.close()
    return

def validar_entero(n):
    if (isinstance(n, int)):
        return True
    else:
        return False

def validar_rango(n, ri, rf):
    if ( validar_entero(n) == True):
        if (n >= ri and n <= rf):
            return True
        else:
            return False
    else:
        return False

def pedir_numero(msg, ri, rf):
    n=""
    while( validar_rango(n, ri, rf) == False):
       n=input(msg)
       if ( n.isdigit() == True):
           n = int(n)
    #fin_while
    return n
#fin_pedir_numero

def pedir_precio(msg, ri, rf):
    n=""
    while( validar_rango(n, ri, rf) == False):
       n=input(msg)
       if ( n.isdigit() == True):
           n = int(n)
    #fin_while
    return n
#fin_pedir_precio

def pedir_nota(msg, ri, rf):
    n=""
    while( validar_rango(n, ri, rf) == False):
       n=input(msg)
       if ( n.isdigit() == True):
           n = int(n)
    #fin_while
    return n
#fin_pedir_nota


def pedir_tiempo_estudio(msg, ri, rf):
    n=""
    while( validar_rango(n, ri, rf) == False):
       n=input(msg)
       if ( n.isdigit() == True):
           n = int(n)
    #fin_while
    return n
#fin_pedir_tiempo_estudio

def pedir_placa(numero):
    numero_invalido=numero[0:4].isdigit()==False or numero[5:8].isdigit()==True or len(numero)!=8
    while (numero_invalido == True):
        numero = input("Ingrese numero de placa(1234-abc) :")
        numero_invalido = numero[0:4].isdigit() == False or numero[5:8].isdigit() == True or len(numero)!=8
    return(numero)

def pedir_ruc(numero):
    numero_invalido = (len(numero) != 11 or numero.isdigit() == False)
    while(numero_invalido==True):
        numero=input("Ingrese numero de RUC:")
        numero_invalido = (len(numero) != 11 or numero.isdigit() == False)
    return (numero)

def pedir_cel(cel):
    cel_invalido = (len(cel) != 9 or cel.startswith("9")==False or cel.isdigit() == False)
    while (cel_invalido == True):
        cel = input("Ingrese numero de celular :")
        cel_invalido = (len(cel) != 9 or cel.startswith("9") == False or cel.isdigit() == False)
    if(len(cel)==9):
        print("Tu numero de celular es:")
    return (cel)

def pedir_dni(numero):
    numero_invalido = (len(numero) != 8 or numero.isdigit() == False)
    while (numero_invalido == True):
        numero = input("ingrese numero de DNI valido:")
        numero_invalido = (len(numero) != 8 or numero.isdigit() == False)
    return (numero)

def pedir_postal(numero):
        numero_invalido = (len(numero) != 5 or numero.isdigit() == False)
        while (numero_invalido == True):
            numero = input("ingrese numero de DNI valido:")
            numero_invalido = (len(numero) != 5 or numero.isdigit() == False)
        return (numero)


def pedir_entero(msg):
    n=-1
    while(validar_entero(n)==False):
        n=int(input(msg))
    #fin_while
    return n
# fin_def

def validar_cadena(cadena):
    # vereficar si el numero es entero
    if(isinstance(cadena,str)):
        # verificar si es entero positivo
        if (cadena>=0):
            return True
        else:
            # si no es positivo retornar false
            return False

    else:
        # si no es cadena return False
        return False
    #fin_if
#fin_def

def pedir_cadena(msg):
    n=-1
    while(validar_cadena(n)==False):
        n=(input(msg))
    #fin_while
    return n
# fin_def


def validar_nombre(nombre):
    # vereficar si el numero es entero
    if(nombre.isdigit==True or len(nombre)<3):
      return False

    else:
      return False

    #fin_if
#fin_def

def pedir_nombre(msg):
    n=-1
    while(validar_nombre(n)==False):
        n=(input(msg))
    #fin_while
    return n
# fin_def


def validar_sexo(sexo):
        # vereficar si el numero es entero
        if (sexo == "masculino" or sexo == "femenino"):

            if (sexo.isdigit() == True):
                return False
            else:
                return True
        else:
            return False

        # fin_if
    # fin_def

def pedir_sexo(msg):
    n=-1
    while(validar_sexo(n)==False):
        n=(input(msg))
    #fin_while
    return n
# fin_def


