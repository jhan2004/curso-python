animales = ["perro","caballo","rana", "dino"]
numeros = [35,25,46,790]

#recorriendo la lista animales 
for animal in animales:
    print(f"ahora la variable animal es igual a: {animal}")

#recorriendo la lista numeros y multiplicandio cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)

#iterando dos listas del mismo tamño al mismo tiempo
for animal,numero in zip(animales,numeros) :
    print(f"recorriendo lista 1: {animal}")
    print(f"recorriendo la lista 2: {numero}")

#forma no optima de recorrer una lista con su indice (no funciona para conjuntos)
for num in range(len(numeros)):
    print(num)

#forma correcta de recorrer una lista con su indice 
for num in enumerate(numeros):
    print(num)
    
#usando for/else 
for numero in numeros:
    print(f"ejecutando el ultimo bucle: {numero}")
else:
    print("el bucle termino")
    
#todo lo anterior funcions igualmente para tuplas y conjuntos 
