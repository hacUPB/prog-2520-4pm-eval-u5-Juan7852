import csv
#crear la lista de temperatura, humedad y presion y leer los datos del archivo
presi=[]
hume=[]
temp=[]
with open('C:\\Users\\B09S202est\\Documents\\variables.csv', 'r') as csvfile:   #usamos el manejador de contexto
    lector = csv.reader(csvfile,delimiter=";") #se utiliza el método reader
    encabezado= next(lector)
    for fila in lector:          #con el for se itera sobre el objeto para leer
        dato= fila[2]#0,84
        dato1=fila[0]
        dato1=int(dato1)
        
        temp.append(dato1)
        dato2=int(fila[1])
        
        hume.append(dato2)
        dato=float(dato.replace(",","."))#0.84
        presi.append(dato)
print(encabezado[2])
print(presi)
print(encabezado[0])
print(temp)
print(encabezado[1])
print(hume)