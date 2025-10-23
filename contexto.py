lista = ["aboutyou","lines","terrified","cuatro","cinco"]
ruta = "C:\\Users\\B09S202est\\Downloads"
#\ secuencia de escape: \n  \t  \ --> \\
file_name = "canciones.txt"
file_info = ruta+"\\"+file_name
modo= "r"

with open(file_info,modo, encoding="utf-8") as archivo:
    for dato in archivo:
        print(dato)
#el archivo se cierra automaticamente al salir del bloque with