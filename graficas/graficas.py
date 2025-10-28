import matplotlib.pyplot as plt
import numpy as np
import math 
# Datos
x = []
y = []
for i in range(100):
    dato=i/100
    x.append(dato)

for j in range (len(x)):
    dato=math.cos(2*math.pi*x[j])
    y.append(dato)

# Crear la gráfica
plt.plot(x, y)

# Agregar título y etiquetas
plt.title('Gráfica de Coseno')
plt.xlabel('X')
plt.ylabel('cos(X)')

# Mostrar la gráfica
plt.show()