
from introducir.numero import solicitar_introducir_numero_extremo
from ejercicios.ejercicio1 import mainej1

def main():
    print("Bienvenido al menú de ejercicios del tema 4")
    print("=" * 50)
    eleccion = solicitar_introducir_numero_extremo("Introduzca el número del ejercicio que desea ejecutar (1-3) (4 para salir)",1,4)
    if eleccion == 1:
        mainej1()
        main()
    elif eleccion == 4:
        exit()
    """elif eleccion == 2:
        mainej2()
        main()
    elif eleccion == 3:
        mainej3()
        main()"""

if __name__ == '__main__':
    main()