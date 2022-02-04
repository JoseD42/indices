import numpy as np

data = np.arange(0, 11)
indice = 7.0

print(data)

print("Indice 0: " + str(data[0]))
print("Indice 3: " + str(data[3]))

#Index out of bounds
#print("Indice 16: " + str(data[16]))

#Si usamos variables en los indices
#Tiene que ser int (numeros enteros)
#Puede ser negativo
print("Indice 'indice': " + str(data[int(indice)]))

#Si usamos negativos, se recorre en resversa
#Comenzando desde el -1
print("Indice -1: " + str(data[-1]))
print("Indice -7: " + str(data[-7]))

#print("Indice -16: " + str(data[-16]))

#Para traer rangos es en la posicion [n:m]
#m se incluye
#n se excluye
#Rnago siempre regresa un arreglo
print("Indice [0:5]: " + str(data[0:5]))
#Me regresa un arreglo vacio
print("Indice [1:1]: " + str(data[1:1]))

print("Indice [1:2]: " + str(data[1:2]))

#Si no le doy rango validos, me regresa vacion
#El final debe ser mayor que el inicio
print("Indice [4:1]: " + str(data[4:1]))
#No existe el indice 11, pero no marca error
#Porque nunca intenta acceder a el
print("Indice [1:11]: " + str(data[1:11]))
#Si te sales de los limites no marca error
#Solo te regresa hasta donde puede
print("Indice [1:16]: " + str(data[1:16]))

#Estos rangos si son validso
#Aunque sean negativos la n siempre es excluyente
print("Indice [1:-1]: " + str(data[1:-1]))
print("Indice [1:-3]: " + str(data[1:-3]))
#El 3er paramentro del rango es el"step"
print("Indice [1:-1:2]: " + str(data[1:-1:2]))

#Los parametros de los rangos, son opcionales
#Si se omite el primero (m) lo toma como el primer elemento
print("Indice [:5]: " + str(data[:5]))
#Si se omite el segundo (n) lo toma como el ultimo elemento
print("Indice [2:]: " + str(data[2:]))
print("Indice [-6:]: " + str(data[-6:]))
#Si se omiten ambos paramertros (m y n) lo toma como
#Solo se contempla el step
print("Indice [::2]: " + str(data[::2]))
#Si los valores del step son negativos
#Primero invierte el arreglo
print("Indice [::-1]: " + str(data[::-1]))
print("Indice [::-2]: " + str(data[::-2]))

elemento = data[5]
elemento = 7
#data[5] = 7
print("Elemento: " + str(elemento))
print("Data: " + str(data))

#Se modifica un segmento obtenido por rango de un ndarray
#Tambien se ve modificadoel ndarray original
segmento = data [1:6:2]
print("Segmento: " + str(segmento))
segmento[0] = 24
print("Segmento Modificado: " + str(segmento))
print("Data: " + str(data))

#Si se modifica el ndarray original
#Tambien se ve modificado el segmento
data[5] = 48
print("Data: " + str(data))
print("Segmento: " + str(segmento))