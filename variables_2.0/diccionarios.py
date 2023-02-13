#creando diccionarios con dict()
diccionario = dict(nombre = "jhan", apellido = "saavedra")

#las listas no pueden ser claves y usamos fronset para meter grupos
diccionario = {frozenset(["jhan","lindo"]):"jajajaj"}

#creando diccionario coon fromkeys() valor por defecto None
diccionario = dict.fromkeys(["nombre","apellido", "deguidores"])

#creando diccionario con fromkeys()con valor "no se"
diccionario = dict.fromkeys(["nombre","apellido", "deguidores"],"no se")


print(diccionario)