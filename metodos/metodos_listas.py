#creando una lista con list()
lista = list(["jhan","carlos",18])

#cuenta la cantidad de los elementos dentro de una lista
cantidad_elementos = len(lista)

#agrega los elementos de la lista 
lista.append("saavedra")

#agregando un alemento a la lista cin indice especifico
lista.insert(4,"2004")

#agregando varios elementos a la lista 
lista.extend(["oneida","yilver"])

#eliminando un elemento de la lista (por su indice)
lista.pop(-1) #-1 para eliminar el ultimo de la lista y asi sucesivamente

#removiendo un elemento de la lista por su valor 
lista.remove("2004")

lista_2 = [12,45,5,9,True,False]

#ordenando la lista de forma ascendente (si le ponemos el parametro reverse=true de invierte el orden)
lista_2.sort()

#invierte los elementos de la lista 
lista_2.reverse()



#eliminandi tidos los elementos de la lista 
#lista.clear()
print(lista)