import json
import sys

nombre =sys.argv[1]
edad = int(sys.argv[2])

datos = json.load(open("../ejemploJSON/datos.json"))

datos["nombre"] = nombre
datos["edad"] = edad

json.dump(datos, open("../ejemploJSON/datos.json", "w"))