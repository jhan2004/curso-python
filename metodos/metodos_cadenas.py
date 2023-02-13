cadena1 = "Soy,Jhan"
cadena2 = "bienvenido maquinola"

#se pone primero el nombre de el objeto luego un . y luego el metodo

#cinvierte a mayusculas 
resultado = cadena1.upper()

#cinvierte a minusculas
resultado2 = cadena1.lower()

#primera letra mayuscula 
resultado3 = cadena1.capitalize()

#buscamos una cadena en otra cadena,si hay coincidencias devuelve la posicion si no devuelve -1
busqueda_find = cadena1.find("J")

#buscamos una cadena en otra si nohay coincidencias devuelve una exepcion
busqueda_index = cadena1.index("J")

#si es numerico nos devuelve true si no nos devuelve false
es_numerico = cadena1.isnumeric()

#si es alpha numerico devuelves true si no devuelve false
es_alphanumerico = cadena1.isalpha()

#contamos las coincidencias de una cadena dentro de otra cadena y  devuelve la cantidad de coincidencia
contar_coincidencias = cadena1.count("a")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true sino false
empieza_con = cadena1.startswith("S")

#verifica si una cadena termina con otra cadena dada, si es asi devuelve true sino false
termina_con = cadena1.endswith("n")

#si el valor 1 esta en la cadena original, reemplaza el valor 1 por el 2
cadena_nueva = cadena1.replace("Soy","yo soy")

#separar cadenas con la cadena que le pasemos 
cadena_separada = cadena1.split(",")

print(cadena_separada)
