from introducir.numero import solicitar_introducir_numero_extremo
from ejercicios.ejercicio1 import mainej1
from ejercicios.ejercicio2 import mainej2
from ejercicios.ejercicio3 import mainej3
from colorama import Fore
import os


def main():
    os.system("cls")
    print(Fore.LIGHTCYAN_EX + "Bienvenido al menú de ejercicios del tema 4")
    print("=" * 50)
    eleccion = solicitar_introducir_numero_extremo(
        "Introduzca el número del ejercicio que desea ejecutar:\n1. StarWars\n2. Pokémon\n3. Siete Maravillas\n4. Salir", 1, 4)
    print(Fore.RESET)
    if eleccion == 1:
        os.system('cls')
        print(Fore.LIGHTMAGENTA_EX + "Poe Dameron, líder del escuadrón negro de la Resistencia, tiene dificultades para transmitir los mensajes a la\nbase de la Resistencia, dado que los mismos son muy largos y los satélites espías de la Primera Orden los intercepta, en un\nlapso muy corto desde que se transmiten. Por lo cual, nos solicita desarrollar un algoritmo que permita comprimir los\nmensajes para enviarlos más rápido y no puedan ser interceptados. Contemplando los siguientes requerimientos, implementar\nun algoritmo que los resuelva:\na.crear un árbol de Huffman a partir de la siguiente tabla:\nb.desarrollar las funciones para comprimir y descomprimir un mensaje.\n", Fore.RESET)
        mainej1()
        main()
    elif eleccion == 2:
        os.system('cls')
        print(Fore.LIGHTMAGENTA_EX + "Se tiene un archivo con los Pokémons de las 8 generaciones cargados de manera desordenada (890 en total) de los\ncuales se conoce su nombre, número, tipo/tipos, debilidad frente a tipo/ tipos, para el cual debemos construir tres\nárboles para acceder de manera eficiente a los datos almacenados en el archivo, contemplando lo siguiente:\na.los índices de cada uno de los árboles deben ser nombre, número y tipo\nb.mostrar todos los datos de un Pokémon a partir de su número y nombre\n(para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar\ntodos los Pokémons cuyos nombres comiencen o contengan dichos caracteres)\nc.mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico.\nrealizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre.\nd.mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum.\ne.mostrar todos los tipos de Pokémons y cuántos hay de cada tipo.\n", Fore.RESET)
        mainej2()
        main()
    elif eleccion == 3:
        os.system('cls')
        print(Fore.LIGHTMAGENTA_EX + "Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas y naturales del mundo,\npara lo cual se deben tener en cuenta las siguientes actividades:\na.de cada una de las maravillas se conoce su nombre,país de ubicación (puede ser más de uno en las naturales) y tipo (natural o arquitectónica)\nb.cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar la distancia que las separa\nc.hallar el árbol de expansión mínimo de cada tipo de las maravillas.\nd. determinar si existen países que dispongan de maravillas arquitectónicas y naturales.\ne. determinar si algún país tiene más de una maravilla del mismo tipo.\nf. deberá utilizar un grafo no dirigido.)\n", Fore.RESET)
        mainej3()
        main()
    elif eleccion == 4:
        os.system('cls')
        exit()


if __name__ == '__main__':
    main()
