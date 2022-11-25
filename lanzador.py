
from introducir.numero import solicitar_introducir_numero_extremo
from ejercicios.ejercicio1 import mainej1
from ejercicios.ejercicio2 import mainej2
from ejercicios.ejercicio3 import mainej3
from colorama import Fore
import os

def main():
    print(Fore.LIGHTCYAN_EX + "Bienvenido al menú de ejercicios del tema 4")
    print("=" * 50)
    eleccion = solicitar_introducir_numero_extremo("Introduzca el número del ejercicio que desea ejecutar (1-3) (4 para salir)",1,4)
    print(Fore.RESET) ; os.system('cls')
    if eleccion == 1:
        print("Poe Dameron, líder del escuadrón negro de la Resistencia, tiene dificultades para transmitir los mensajes a la\nbase de la Resistencia, dado que los mismos son muy largos y los satélites espías de la Primera Orden los intercepta, en un\nlapso muy corto desde que se transmiten. Por lo cual, nos solicita desarrollar un algoritmo que permita comprimir los\nmensajes para enviarlos más rápido y no puedan ser interceptados. Contemplando los siguientes requerimientos, implementar\nun algoritmo que los resuelva:\n\na.crear un árbol de Huffman a partir de la siguiente tabla:\n\nb.desarrollar las funciones para comprimir y descomprimir un mensaje.\n")
        mainej1()
        main()
    elif eleccion == 2:
        print("Se tiene un archivo con los Pokémons de las 8 generaciones cargados de manera desordenada (890 en total) de los\ncuales se conoce su nombre, número, tipo/tipos, debilidad frente a tipo/ tipos, para el cual debemos construir tres\nárboles para acceder de manera eficiente a los datos almacenados en el archivo, contemplando lo siguiente:\na.los índices de cada uno de los árboles deben ser nombre, número y tipo\nb.mostrar todos los datos de un Pokémon a partir de su número y nombre\n(para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres)\nc.mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico.\nrealizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombree.\nd.mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrumf.\ne.mostrar todos los tipos de Pokémons y cuántos hay de cada tipo.\n")
        mainej2()
        main()
    elif eleccion == 4:
        exit()
    elif eleccion == 3:
        mainej3()
        main()

if __name__ == '__main__':
    main()