file = input("Ingrese la ruta del archivo: ")
row = int(input("Ingrese la ultima fila a leer: "))

archivo = open(file)

while row>0:
 row -= 1
 linea=archivo.readline()
 print(linea)

archivo.close()