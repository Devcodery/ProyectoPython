import json
from pathlib import Path

ruta = Path.parents()

print(f"ruta: {ruta}")

for archivo in ruta.rglob("*.json"):
    print(f"Archivo: {archivo}")
   