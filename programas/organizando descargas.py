import os
import shutil

# Ruta de la carpeta de descargas
ruta_descargas = "C:/Users/Usuario/Downloads"

# Lista de extensiones y las carpetas correspondientes
extensiones = {
    '.pdf': 'Documentos',
    '.docx': 'Documentos',
    '.xlsx': 'Documentos',
    '.pptx': 'Documentos',
    '.psd': 'Documentos',
    '.jpg': 'Imágenes',
    '.jpeg': 'Imágenes',
    '.png': 'Imágenes',
    '.gif': 'Imágenes',
    '.webp': 'Imágenes',
    '.mp4': 'Videos',
    '.avi': 'Videos',
    '.mkv': 'Videos',
    '.mp3': 'Música',
    '.wav': 'Música',
    '.zip': 'Archivos comprimidos',
    '.rar': 'Archivos comprimidos',
    '.exe': 'Programas',
    '.msi': 'Programas',
}

# Recorre todos los archivos de la carpeta de descargas
for archivo in os.listdir(ruta_descargas):
    # Ignora los archivos ocultos
    if archivo.startswith('.'):
        continue
    
    # Obtiene la extensión del archivo
    extension = os.path.splitext(archivo)[1].lower()
    
    # Si la extensión del archivo está en la lista de extensiones conocidas
    if extension in extensiones:
        # Obtiene la carpeta de destino
        carpeta_destino = os.path.join(ruta_descargas, extensiones[extension])
        
        # Si la carpeta de destino no existe, la crea
        if not os.path.exists(carpeta_destino):
            os.mkdir(carpeta_destino)
        
        # Mueve el archivo a la carpeta de destino
        origen = os.path.join(ruta_descargas, archivo)
        destino = os.path.join(carpeta_destino, archivo)
        shutil.move(origen, destino)

print('La organización de archivos se ha completado con éxito.')