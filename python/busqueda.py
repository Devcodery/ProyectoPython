import json
from pathlib import Path

ruta = Path.cwd() / "tienda"

print(f"ruta: {ruta}")

for archivo in ruta.glob("*.json"):
    print(f"Archivo: {archivo}")
   