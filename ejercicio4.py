import csv

def lineas(archivo):
	return csv.reader(archivo, delimiter=";")

with open("data/data-estudiantes.csv") as midata:
	print(list(map(lambda x: x[1], filter(lambda x: x[1] != "email", lineas(midata)))))

# midata = open("data/data-estudiantes.csv") # en usos de grande volumenes de \
	# datos es necesario cerrer el archivo
	# print(list(lineas(midata)))
	# midata.close()