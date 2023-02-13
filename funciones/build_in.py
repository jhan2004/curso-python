numeros = [9,5,8,6,7,3,19,60]

#encontrando el numero mayor de una lista 
numero_mas_alto = max(numeros)
#print(numero_mas_alto)

#encontrando el numero mas bajo de una lista 
numero_mas_bajo = min(numeros)
#print(numero_mas_bajo)

#redondeando a 6 decimales 
numero = round(15.456969,2)
#print(numero)

#retorno false => 0, vacio, false, None / True => distinto a 0, true -
#cadena o datos no vacios
resutado_bool = bool()
#print(resutado_bool)

#retorna true si todos los valores sin verdaderos
#resultado_all = all([0,"True",[300,30]])

#suma todos los valores de un iterable (sum max y min solo fucionan con numaeros)
suma_total = sum(numeros)
print(suma_total)
