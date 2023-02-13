diccionario = {
    "nombre" : "jhan",
    "apellido" : "saavedra",
    "edad" : 18
}

#nos devuelve un objeto dic_item
claves = diccionario.keys()

#obteniendo un elemento con (get) sino encuentra nada el programa continua
claves = diccionario.get("nombre")

#eliminando todo de el diccionario
diccionario.pop("edad")

print(diccionario)