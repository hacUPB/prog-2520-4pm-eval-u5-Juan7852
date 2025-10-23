ruta = "C:\\Users\\B09S202est\\Downloads"
#\ secuencia de escape: \n  \t  \ --> \\
file_name = "aviones1.txt"
modo= "x"
fp = open(ruta+"\\"+file_name,modo, encoding="utf-8")
nombre = input("ingrese el nombre de lavion: ")
peso = int(input("ingrese el peso del avion: "))
velocidad = float(input("velocidad maxima: "))
fp.write(nombre+"\n")
fp.write(str(peso)) #los argumentos ya deben ser stream 
fp.write("\n")
fp.write(str(velocidad)+"\n\n")
#fp.write(nombre+"\n"+peso+"\n"+velocidad)
fp.close()