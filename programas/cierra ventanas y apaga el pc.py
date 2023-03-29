import os

# Cierra todas las ventanas abiertas
os.system('taskkill /f /im explorer.exe')

# Apaga el PC
os.system('shutdown /s /t 0')
