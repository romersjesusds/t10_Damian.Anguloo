import libreria
assert (libreria.validar_dni("") == False)
assert (libreria.validar_dni("12233") == False)
assert (libreria.validar_dni("76582734") == True)
assert (libreria.validar_dni("holamundo") == False)
print("esta ok")

assert (libreria.validar_lugar("morrope") == True)
assert (libreria.validar_lugar("12233") == False)
assert (libreria.validar_lugar(True) == False)
assert (libreria.validar_lugar("ho") == False)
print("esta ok")

assert (libreria.validar_nombre("Roberto") == True)
assert (libreria.validar_nombre("1999999") == False)
assert (libreria.validar_nombre(False) == False)
assert (libreria.validar_nombre("fr") == False)
print("esta ok")

assert (libreria.validar_telefono("970792170") == True)
assert (libreria.validar_telefono("9838839393") == False)
assert (libreria.validar_telefono("holaaaaaa") == False)
assert (libreria.validar_telefono("9878") == False)
print("esta ok")

assert (libreria.validar_entero(2018) == True)
assert (libreria.validar_entero("hola") == False)
assert (libreria.validar_entero(-455) == False)
assert (libreria.validar_entero(False) == False)
print("esta ok")

assert (libreria.validar_codigo("192023E") == True)
assert (libreria.validar_codigo("hola") == False)
assert (libreria.validar_codigo("288393909A") == False)
assert (libreria.validar_codigo(12333211) == False)
print("esta ok")

assert (libreria.validar_real(23.3) == True)
assert (libreria.validar_real("hola") == False)
assert (libreria.validar_real(True) == False)
assert (libreria.validar_real(12333211) == False)
print("esta ok")

assert (libreria.validar_cadena("192023E") == True)
assert (libreria.validar_cadena("hola") == True)
assert (libreria.validar_cadena(212.23) == False)
assert (libreria.validar_cadena(12333211) == False)
assert (libreria.validar_cadena(True) == False)
print("esta ok")


assert (libreria.validar_capital("lima") == True)
assert (libreria.validar_capital(23.32) == False)
assert (libreria.validar_capital(True) == False)
assert (libreria.validar_capital(12333211) == False)
print("esta ok")


