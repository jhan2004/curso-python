#
def frase(nombre,apellido,adjetivo):
    return f"hola {nombre} {apellido} sos muy {adjetivo}"

palabra_resultante = frase("jhan","saavedra","capo")
print(palabra_resultante)

#podemos poner una funcion con parametros predeterminados en este caso el 
#adjetivo, (lo podemos cambiar si queremos)
def frase(nombre,apellido,adjetivo="lindo"):
    return f"hola {nombre} {apellido} sos muy {adjetivo}"

palabra_resultante2 = frase("jhan","saavedra",)
print(palabra_resultante2)