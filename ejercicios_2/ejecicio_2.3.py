#Escribir un programa que pregunte al usuario una cantidad a invertir,
#el interés anual y el número de años, y muestre por pantalla el capital
#obtenido en la inversión.

inversion_total = int(input("cuanto dinero vas a invertir: "))
interes_anual = float(input("cual es el interes anual (solo numeros): "))
tiempo_de_inversion = int(input("numero de años que va a durar tu inversion: "))

print(f"su capital obtenido es: {round((inversion_total * interes_anual) * tiempo_de_inversion,2)}")