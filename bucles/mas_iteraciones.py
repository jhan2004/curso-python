frutas = ["banana","naranja","manzana","durazno","pera"]
cadena = "hola Jhan"
numeros = [2,5,8,10]

#evitamos que se coma una manzana con la sentacia continue
for fruta in frutas:
    if fruta == "manzana":
        continue
    print(f"me voy a comer una: {fruta}")
    
print("hola")
    
#evitar que el bucle siga ejecutandose 
for fruta in frutas:
    if fruta == "manzana":
        break
    print(f"ma voy a comer una: {fruta}")
    
print("bucle terminado")

#recorriendo una cadena 
for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo 
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)