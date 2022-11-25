
from introducir.numero import solicitar_introducir_numero_extremo
from ejercicios.ejercicio1 import mainej1
from colorama import Fore
import os

def main():
    print(Fore.LIGHTCYAN_EX + "Bienvenido al menú de ejercicios del tema 4")
    print("=" * 50)
    eleccion = solicitar_introducir_numero_extremo("Introduzca el número del ejercicio que desea ejecutar (1-3) (4 para salir)",1,4)
    print(Fore.RESET) ; os.system('cls')
    if eleccion == 1:
        print("""Poe Dameron, líder del escuadrón negro de la Resistencia, tiene dificultades para transmitir los mensajes a la\nbase de la Resistencia, dado que los mismos son muy largos y los satélites espías de la Primera Orden los intercepta, en un\nlapso muy corto desde que se transmiten. Por lo cual, nos solicita desarrollar un algoritmo que permita comprimir los\nmensajes para enviarlos más rápido y no puedan ser interceptados. Contemplando los siguientes requerimientos, implementar\nun algoritmo que los resuelva:\n\na.crear un árbol de Huffman a partir de la siguiente tabla:\n\nb.desarrollar las funciones para comprimir y descomprimir un mensaje.\n""")
        mainej1()
        main()
    elif eleccion == 2:
        import ejercicios.ejercicio2
    elif eleccion == 4:
        exit()
    """elif eleccion == 3:
        mainej3()
        main()"""

if __name__ == '__main__':
    main()