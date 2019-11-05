import csv

def lineas_diccionario(archivo):
	return csv.DictReader(archivo, delimiter=";")

with open("data/data-estudiantes.csv") as midata:
	resultado = list(lineas_diccionario(midata))

	nombres = list(map(lambda x: list(x.items())[0][1].split()[1], resultado)) # Muestra Nombres
	correos = list(map(lambda x: list(x.items())[1][1].strip(".com"), resultado)) # Muestra correos

	print(nombres, "\n\n")
	print(correos, "\n\n")
	# Cadena a presentar
	newlist = list(map(lambda x: "%s - %s" %(list(x.items())[0][1].split(" ")[1], \
		list(x.items())[1][1].strip(".com")), resultado))
	print(newlist)
	#newlist = list(map(""))
	#cadena = "ads@hotmail.com"
	#print(cadena.strip(".com"))
