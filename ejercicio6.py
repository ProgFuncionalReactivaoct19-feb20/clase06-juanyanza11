"""
	- Filtrar los registros cuyos países tengan en su nombre una longitud mayor a 10

	- Ordenar la lista en función del día de nacimiento.
	author = juanyanza11
"""
import csv

def lineas_diccionario(archivo):
	return csv.DictReader(archivo, delimiter="\t")

with open("data/trabajadores.csv") as midata:
	resultado = list(lineas_diccionario(midata))

	# Posición de la cadena para validar si es mayor a 10 el tamaño de la misma
	funcion = filter(lambda x: len(list(x.items())[2][1])> 10, resultado)
	print("Nombres con longitud mayor a 10\n",list(funcion),"\n\n")

	newl = list(filter(lambda x: list(x.items()), resultado)) # Lista en la posición de la fecha de nacimiento
	order = sorted(newl, key = lambda x: list(x.items())[1][1].split("-")[2]) # Ordenar por día de nacimiento

	print("Ordenado por día de nacimiento\n",order)