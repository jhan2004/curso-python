import os

# Cierra todas las ventanas abiertas
os.system('taskkill /f /im explorer.exe')

# Pregunta al usuario si desea apagar el PC
opcion = input("¿Desea apagar el PC? (Sí/No)")

if opcion.lower() == "sí":
    # Apaga el PC
    os.system('shutdown /s /t 0')
else:
    print("El PC no se apagará.")
    