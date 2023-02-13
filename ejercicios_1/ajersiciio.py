#1. Luis compró 8 cuadernos a 25 
# pesos cada uno y 7 bolígrafos. 
# En total se gastó 298 pesos, ¿cuánto
# costó cada bolígrafo?

cuadernos_comprados = 8
boligrafos_comprados = 7
gasto_total = 298 
valor_de_cada_boligrafo = 0

valor_boligrafos = 298 - cuadernos_comprados * 25
valor_de_cada_boligrafo = valor_boligrafos / boligrafos_comprados


print(f"cada boligrafo cuesta {valor_de_cada_boligrafo} pesos")