#Escribir un programa que pida al usuario su peso (en kg) y estatura
#(en metros), calcule el índice de masa corporal y lo almacene en una 
#variable, y muestre por pantalla la frase Tu índice de masa corporal 
#es <imc> donde <imc> es el índice de masa corporal calculado redondeado 
#con dos decimales.

nombre = input("¿cual es tu nombre?: ")

peso_en_kg = int(input(f"hola {nombre}, ¿cual es tu peso en kg?: "))
altura_en_m = float(input("dime cual es tu altura en metros: "))
imc = peso_en_kg / altura_en_m 

print(f"{nombre}, tu imc es igual a : {round(imc,2)}")

