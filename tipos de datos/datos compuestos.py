#esta es una lista y puedo acceder asus datos por el indice 
lista = ["jhan","soy jhan",1.80]
print(lista[0])

#creando una tupla (no se pueden modificar)
tupla = {"jhan","soy jhan",1.80}

#creando un conjunto (set) (no se puede llamar a los elemetos por indice y no almacena datos duplicados)
conjunto = {"jhan","jhan","soy jhan",1.80}
#print(conjunto[3])esto no se puede,(no puede acceder al por indice)

print(conjunto)

#creando diccionario (dict)
#(la estructura es key : value y separamos con comas)
diccionario = {
    'nombre' : "jhan saavedra ",
    'canal' : "jhan ss",
    'esta programando' : True
}
print(diccionario['nombre'])

