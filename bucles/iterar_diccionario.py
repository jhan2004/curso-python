diccionario = {
    "nombre" : "jhan",
    "apellido" : "saavedra",
    "seguidores" : 5
}

#recorriendo el diccionario para obtener las claves  
for key in diccionario:
    print(f"la clave es: {key}")
    
#recorriendo el diccionario con items() para obtener las claves y el valor 
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor es: {value}")


