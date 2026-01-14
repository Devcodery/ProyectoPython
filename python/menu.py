import curses # Importa la biblioteca curses para manejo de interfaces de texto
from pathlib import Path
import subprocess
from time import sleep

def opcion1():
    strcreen.clear()
    strcreen.addstr("Has seleccionado la Opción 1\n")
    strcreen.addnstr("Presiona cualquier tecla para volver al menú", 50)
    strcreen.getch()

def opcion2():
    strcreen.clear()
    strcreen.addstr("Has seleccionado la Opción 2\n")
    strcreen.addnstr("Presiona cualquier tecla para volver al menú", 50)
    strcreen.getch()
    
def opcion3():
    strcreen.clear()
    strcreen.addstr("Has seleccionado la Opción 3\n")
    strcreen.addnstr("Presiona cualquier tecla para volver al menú", 50)
    strcreen.getch()
    
def listar():
    strcreen.clear()
    strcreen.addstr("Has seleccionado Listar\n")
    PATH = Path.home() / "Descargas/tienda"
    
    path = PATH
    
    seleccion = 0
    salirBucle = True
    
    while salirBucle:
        
        strcreen.clear()
        elementos = [path.parent] + sorted(path.iterdir())
        
        if elementos[0].name == "Descargas":
            elementos.remove(elementos[0])
            
        for i, elemento in enumerate(elementos):
            elemento1 = elemento.name
            
            if elemento == path.parent:
                elemento1 = "Volver"
            if i == seleccion:
                strcreen.addstr(i + 2, 0, f"> {elemento1}", curses.A_REVERSE)
            else:
                strcreen.addstr(i + 2, 0, f"  {elemento1}")
        
        strcreen.addstr(len(elementos) + 3, 0, "Salir (Presiona 'q')")
        
        if path.name == "Categoria":    
            strcreen.addstr(len(elementos) + 5, 0, "Presiona 'c' para crear una nueva categoria")
            strcreen.addstr(len(elementos) + 6, 0, "Presiona 'r' para renombrar una nueva categoria")
            
        strcreen.addstr(len(elementos) + 9, 0, f"El elemento seleccionado es: {elementos[seleccion]}")
        strcreen.addstr(len(elementos) + 10, 0, f"El elemento donde me encuentro es: {path}")
        
        teclaListar = strcreen.getch()
        
        if teclaListar == curses.KEY_DOWN and seleccion < len(elementos) - 1:
            seleccion += 1
        elif teclaListar == curses.KEY_UP and seleccion > 0:
            seleccion -= 1
        elif teclaListar == ord('c'):
            curses.endwin()
            subprocess.run(["bash", "./script/bash/DAM/crearCarpeta.sh", str(path)])
            
            sleep(5)
        elif teclaListar == ord('r'):
            curses.endwin()
            subprocess.run(["bash", "./script/bash/DAM/cambiarNombre.sh", str(path), str(elementos[seleccion]), str(elementos[seleccion].name)])
            
            sleep(5)
        elif teclaListar == ord('d'):
            pass
        elif teclaListar == ord('\n'):
                path = elementos[seleccion]
                seleccion = 0
        elif teclaListar == ord('q'):
            salirBucle = False
            
            
           
def Salir():
    opcionSalir = ["Si", "No"]
    seleccionSalir = 0
    salirBucle = True
                
    while salirBucle:
        strcreen.clear()
        strcreen.addstr("¿Estás seguro que deseas salir?")
                    
        for i, opcion in enumerate(opcionSalir):
            if i == seleccionSalir:
                strcreen.addstr(4, i * 8, f"> {opcion}", curses.A_REVERSE)
            else:
                strcreen.addstr(4, i * 8, f"  {opcion}")
                            
        teclaSalir = strcreen.getch()
                    
        if teclaSalir == curses.KEY_RIGHT and seleccionSalir < len(opcionSalir) - 1:
            seleccionSalir += 1
        elif teclaSalir == curses.KEY_LEFT and seleccionSalir > 0:
            seleccionSalir -= 1
        elif teclaSalir == ord('\n'):
            if seleccionSalir == 0:
                salirBucle = False
                return False
            else:
                salirBucle = False
                return True


def menu(strcreen):
    opciones = ["Opción 1", "Opción 2", "Opción 3", "Listar", "Salir"]
    
    seleccion = 0
    salirBucle = True
        
    while salirBucle:

        # Limpia la pantalla
        strcreen.clear()
        
        strcreen.addstr("Menu Principal")
        
        for i, opcion in enumerate(opciones):
            if i == seleccion:
                strcreen.addstr(i + 2, 0, f"> {i+1}. {opcion}", curses.A_REVERSE)
            else:
                strcreen.addstr(i + 2, 0, f"{i+1}. {opcion}")
        
        tecla = strcreen.getch()
        
        if tecla == ord('q'):
            break
        elif tecla == curses.KEY_DOWN and seleccion < len(opciones) - 1:
            seleccion += 1
        elif tecla == curses.KEY_UP and seleccion > 0:
            seleccion -= 1
        elif tecla == ord('\n'):
            strcreen.addstr(len(opciones) + 4, 0, f"Seleccionaste: {opciones[seleccion]}")
            if seleccion == 0:
                opcion1()
            elif seleccion == 1:
                opcion2()
            elif seleccion == 2:
                opcion3()
            elif seleccion == 3:
                listar()
            elif seleccion == 4:
                salirBucle = Salir()
    
    
if __name__ == "__main__":
    #Inicia curses y obtiene la pantalla principal
    strcreen = curses.initscr()
    
    #Activar deteccion de teclas especiales
    strcreen.keypad(True)
    
    curses.noecho()  # Desactiva la visualización de las teclas presionadas
    
    curses.cbreak()  # Permite la lectura inmediata de las teclas presionadas
    
    curses.curs_set(0)  # Oculta el cursor
    
    try:
        menu(strcreen)
    finally:
        # Restaurar la configuración de la terminal al salir
        curses.nocbreak()
        strcreen.keypad(False)
        curses.echo()
        curses.endwin()
    