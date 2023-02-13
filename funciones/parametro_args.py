#utilizando el parametro args
#forma optima de sumar valores 
def suma_total(numeros):
    return sum([*numeros])
resultado2 = suma_total([2,4,6,7,9])
print(resultado2)

#lo mismo de arriba bajo el argumento (*args)
def suma(nombre,*numeros):
    return f"{nombre}, la suma de sus numeros es:{sum(numeros)}"

resultado = suma("jhan",4,5,6,7)
#print(resultado)

