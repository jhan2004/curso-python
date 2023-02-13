#creando una fincion simple 
#def saludar():
    #print("hola a todos sean bienvenidos")
    
#ejecutando la funcion simple
#saludar()

#creando un a funcion que tenga parametros 
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        adjetivo = "reina"
    elif sexo == "hombre":
        adjetivo = "titan"
    else:
        adjetivo = "amor"
    print(f"hola {nombre}, mi {adjetivo} ¿como estas?")
    
saludar("jhan","hombre")

#crar una funcion que retorne valores

#
