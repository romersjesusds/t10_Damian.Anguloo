#validar entero
def validar_entero(numero_positivo):
    if(isinstance(numero_positivo,int)==True and isinstance(numero_positivo,bool)==False and numero_positivo>=0):
        return True
    else:
        return False
    #fin if
#fin def

#validar real
def validar_real(numero_real):
    if(isinstance(numero_real,float)==True and isinstance(numero_real,bool)==False):
        return True
    else:
        return False
    #fin if
#fin def

def pedir_real(msg):
    nro_real=True
    while(validar_real(nro_real)==False):
        nro_real=float(input(msg))
    return nro_real

#validar cadena
def validar_cadena(cad):
    if(isinstance(cad,str)==True and isinstance(cad,bool)==False):
        return True
    else:
        return False
    #fin if
#fin def

def pedir_cadena(msg):
    cad=0
    while(validar_cadena(cad)==False):
        cad=input(msg)
    return cad


#validar booleano
def validar_booleano(boll):
    if(isinstance(boll,bool)==True):
        return True
    else:
        return False
    #fin if
#fin def


#funcion que valida si el año es valido
def validar_anio(anio):
    #1. verificar si la cadena tiene forma de digito
    #2. la longitud debe ser 4
    #3. debe ser >0 y <=9999
    if(anio.isdigit()==True):
        if(len(anio)==4):
            anio=int(anio)
            if(anio>0 and anio<=9999):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
#fin def

def pedir_anio(msg):
    anio=-1
    while(validar_anio(anio)==False):
        anio=input(msg)
    return anio



#validar DNI
def validar_dni(dni):
    #verificar si la cadena tiene forma de digito
    #la longitud de la cadena es 8
    if(len(dni)==8):
        if(dni.isdigit()==True):
            return True
        else:
            return False
    else:
        return False
#fin def

def pedir_dni(msg):
    dni=""
    while ( validar_dni(dni) == False ):
        dni=input(msg)
    #fin_while
    return dni
#fin_pedir_dni

#validar sexo
def validar_sexo(sexo):
    if(isinstance(sexo,str)==True):
        cad=sexo.upper()
        if(cad=="MASCULINO" or cad=="FEMENINO"):
            return True
        else:
            return False
    else:
        return False
#fin def

def pedir_sexo(msg):
    sexo=""
    while ( validar_sexo(sexo) == False ):
        sexo=input(msg)
    #fin_while
    return sexo
#fin_pedir_sexo

#validar nombre
def validar_nombre(nombre):
    if(isinstance(nombre,str)==True and nombre.isdigit()==False):
        if(len(nombre)>=3):
            return True
        else:
            return False
    else:
        return False

def pedir_nombre(msg):
    nombre=""
    while ( validar_nombre(nombre) == False ):
        nombre=input(msg)
    #fin_while
    return nombre
#fin_pedir_nombre

#fin def

#validar telefono
def validar_telefono(telefono):
    if(len(telefono)==9):
        if(telefono.isdigit()==True):
            return True
        else:
            return False
    else:
        return False
#fin def

def pedir_telefono(msg):
    telefono=""
    while ( validar_telefono(telefono) == False ):
        telefono=input(msg)
    #fin_while
    return telefono
#fin_pedir_telefono

#validar nota
#devuelve True si la nota es vigesimal


#pedir entero
def pedir_entero(msg):
    n=-1
    while(validar_entero(n)==False):
        n=input(msg)
        if(n.isdigit()==True):
            n=int(n)
    return int(n)
#fin_def


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
    return lista

def agregar_datos (ruta_archivo, contenido,modo):
    archivo=open(ruta_archivo,modo)
    archivo.write(contenido)
    archivo.close()

def mostrar_datos (ruta_archivo):
    archivo=open(ruta_archivo, "r")
    datos=archivo.read()
    archivo.close()
    return datos


def validar_lugar(lugar):
    if(isinstance(lugar,str)==True and lugar.isdigit()==False):
        if(len(lugar)>=3):
            return True
        else:
            return False
    else:
        return False

def pedir_lugar(msg):
    lugar=""
    while ( validar_lugar(lugar) == False ):
        lugar=input(msg)
    #fin_while
    return lugar
#fin_pedir_nombre

def validar_capital(capital):
    if(isinstance(capital,str)==True and capital.isdigit()==False):
        if(len(capital)>=3):
            return True
        else:
            return False
    else:
        return False

def pedir_capital(msg):
    capital=""
    while ( validar_capital(capital) == False ):
        capital=input(msg)
    #fin_while
    return capital
#fin_pedir_nombre

#fin def


#validar nombre
def validar_correo(correo):
    data=""
    # 1. Revisar que este dividido por 2 puntos
    data=correo.split(".")
    if ( len(data) != 3):
        return False

    # 2. Los 3 deben ser cadenas
    cad1= data[0]
    cad2= data[1]
    cad3= data[2]
    if ( isinstance(cad1, str) == False and isinstance(cad2, str) == False and
            isinstance(cad3, str) == False):
        return False


def pedir_correo(msg):
    correo=""
    while ( validar_correo(correo) == False ):
        correo=input(msg)
    #fin_while
    return correo
#fin_pedir_nombre

#fin def

def validar_codigo(cad):
    if(isinstance(cad,str)==True and isinstance(cad,bool)==False):
        if(len(cad)==7):
            return True
        else:
            return False
    else:
        return False
    #fin if
#fin def

def pedir_codigo(msg):
    cad=0
    while(validar_codigo(cad)==False):
        cad=input(msg)
    return cad
