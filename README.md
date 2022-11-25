<h1 align = "center"> Evaluación Tema 4</h1>

En este [repositorio](https://github.com/Diegodesantos1/Evaluacion_Tema_4) quedan resueltos los ejercicios de evaluación Tema 4 

<h2 align = "center"> Ejercicio 1: Poe dameron</h2>

![image](https://user-images.githubusercontent.com/91721855/203891239-42cd8012-b113-4e3c-8dec-3fbe19b22d6e.png)
![image](https://user-images.githubusercontent.com/91721855/203891290-a35c04b9-68d1-4dd4-8dc9-31d156db4218.png)
![image](https://user-images.githubusercontent.com/91721855/204056099-2407aaab-8032-4159-8b58-417db732a589.png)

El código empleado es el siguiente:

```python
import os
from colorama import Fore
from clases.huffman import nodoArbolHuffman
from introducir.numero import solicitar_introducir_numero_binario, solicitar_introducir_numero_extremo
from introducir.cadena import solicitar_introducir_cadena_especial


class Ejercicio1:
    os.system('cls')
    tabla_probabilidades = [['A', 0.2], ['F', 0.17], ['1', 0.13], [
        '3', 0.21], ['0', 0.05], ['M', 0.09], ['T', 0.15]]

    diccionario_convertido = {'A': '00', '3': '01', '1': '100',
                              'T': '110', 'F': '111', '0': '1010', 'M': '1011'}

    bosque = []

    for elemento in tabla_probabilidades:
        nodo = nodoArbolHuffman(elemento[0], elemento[1])
        bosque.append(nodo)
    while(len(bosque) > 1):
        elemento1 = bosque.pop(0)
        elemento2 = bosque.pop(0)
        nodo = nodoArbolHuffman('', elemento1.valor+elemento2.valor)
        nodo.izq = elemento1
        nodo.der = elemento2
        bosque.append(nodo)

    def generar_tabla(raiz, cadena=''):
        if(raiz is not None):
            if(raiz.izq is None):
                print(raiz.info, cadena)
            else:
                cadena += '0'
                Ejercicio1.generar_tabla(raiz.izq, cadena)
                cadena = cadena[0:-1]
                cadena += '1'
                Ejercicio1.generar_tabla(raiz.der, cadena)

    def descodificar(cadena, arbol_huff):
        cadena_deco = ''
        raiz_aux = arbol_huff
        pos = 0
        while(pos < len(cadena)):
            if(cadena[pos] == '0'):
                raiz_aux = raiz_aux.izq
            else:
                raiz_aux = raiz_aux.der
            pos += 1
            if(raiz_aux.izq is None):
                cadena_deco += raiz_aux.info
                raiz_aux = arbol_huff
            cadena_deco
        return cadena_deco

    def codificar(cadena, diccionario_convertido):
        cadena_cod = ''
        for caracter in cadena:
            cadena_cod += diccionario_convertido[caracter]
        return cadena_cod


def mainej1():
    eleccion = solicitar_introducir_numero_extremo("1. Mostrar Tabla de Probabilidades y codificación\n2. Descodificar el mensaje\n3. Codificar el mensaje\n4. Salir", 1, 4)
    if eleccion == 1:
        print(Fore.GREEN + "La tabla de probabilidades es: ", Fore.RESET)
        for elemento in Ejercicio1.tabla_probabilidades:
            print(elemento[0], elemento[1])
        print("-" * 50)
        print(Fore.GREEN + "La tabla de codificación es:", Fore.RESET)
        Ejercicio1.generar_tabla(Ejercicio1.bosque[0])
        print("-"*50)
        mainej1()
    if eleccion == 2:
        cadena_descodificar = solicitar_introducir_numero_binario(
            'Ingrese la cadena a decodificar en binario')
        cadena_descodificar = str(cadena_descodificar)
        print(Fore.LIGHTYELLOW_EX + 'La cadena descodificada es:',
            Ejercicio1.descodificar(cadena_descodificar, Ejercicio1.bosque[0]), Fore.RESET)
        cadena_descodificar = str(cadena_descodificar)
        print("-"*50)
        mainej1()
    if eleccion == 3:
        cadena_codificar = solicitar_introducir_cadena_especial(
            'Ingrese la cadena a codificar solo usando A,F,1,3,0,M,T')
        print(Fore.LIGHTYELLOW_EX + 'La cadena codificada es:',
            Ejercicio1.codificar(cadena_codificar, Ejercicio1.diccionario_convertido))
        print(Fore.RESET)
        print("-"*50)
        mainej1()
    if eleccion == 4:
        pass
```

<h2 align = "center"> Ejercicio 2: Pokemon</h2>

![image](https://user-images.githubusercontent.com/91721855/204055851-51ac6deb-4ef9-43e0-ad62-481de2b24b7b.png)
![image](https://user-images.githubusercontent.com/91721855/204056139-453f1ea1-ddd6-4e99-8055-7c87e47beaee.png)

El código empleado es el siguiente:

```python
from clases.arbolbinario import insertar_nodo
from clases.cola import Cola, arribo, atencion, cola_vacia
from introducir.numero import solicitar_introducir_numero_extremo
from introducir.cadena import solicitar_introducir_cadena
import csv
import random
arbol_nombres = None
arbol_tipo = None
arbol_numero = None
lista = []

with open('dataset/pokemon.csv', newline='') as File:
    reader = csv.reader(File)
    datos = list(reader)

nombre = []
for i in range(1, len(datos)):
    nombre.append(datos[i][1])
class Pokemon(object):

    def __init__(self, nombre, numero, tipo, debilidad):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo
        self.debilidad = debilidad

    def __str__(self):
       return self.nombre + ' ' + str(self.numero) + ' ' + self.tipo + ' ' + self.debilidad

def inorden_numero(raiz):
    if(raiz is not None):
        inorden_numero(raiz.izq)
        print(raiz.info[1], raiz.info[0])
        inorden_numero(raiz.der)

def busqueda_proximidad_poke(raiz, buscado):
    if(raiz is not None):
        if(raiz.info[1][0:len(buscado)] == buscado):
            print(raiz.info[1])
            lista.append(raiz.info[1])
        busqueda_proximidad_poke(raiz.izq, buscado)
        busqueda_proximidad_poke(raiz.der, buscado)

def busqueda_proximidad_poke2(raiz, buscado):
    if(raiz is not None):
        if(raiz.info[1][0:len(buscado)] == buscado):
            print(raiz.info[0].nombre)
        busqueda_proximidad_poke2(raiz.izq, buscado)
        busqueda_proximidad_poke2(raiz.der, buscado)

def busqueda_proximidad_poke3(raiz, buscado):
    if(raiz is not None):
        if(raiz.info[0].debilidad[0:len(buscado)] == buscado):
            print(raiz.info[0].nombre)
        busqueda_proximidad_poke3(raiz.izq, buscado)
        busqueda_proximidad_poke3(raiz.der, buscado)

def inorden_nombre(raiz):
    if(raiz is not None):
        inorden_nombre(raiz.izq)
        print(raiz.info[0])
        inorden_nombre(raiz.der)

def por_nivel_nombre(raiz):
    cola = Cola()
    arribo(cola, raiz)
    while(not cola_vacia(cola)):
        nodo = atencion(cola)
        print(nodo.info[0])
        if(nodo.izq is not None):
            arribo(cola, nodo.izq)
        if(nodo.der is not None):
            arribo(cola, nodo.der)

def inorden_tipo(raiz, cont):
    if(raiz is not None):
        if raiz.info[0].tipo == 'fuego':
            cont += 1
        inorden_tipo(raiz.izq, cont)
        print(raiz.info[0].nombre, raiz.info[0].tipo)
        inorden_tipo(raiz.der, cont)
    return cont


tipo = ['agua', 'fuego', 'tierra', 'electrico', 'planta', 'hada', 'volador', 'dragon', 'fantasma', 'siniestro', 'lucha', 'roca', 'psiquico', 'bicho', 'normal', 'veneno', 'acero']
debil = ['agua', 'fuego', 'tierra', 'electrico', 'planta','Jolteon', 'Lycanroc', 'Tyrantum']


for i in range (0, len(nombre)):
    pokemon = Pokemon(nombre[i], random.randint(1, len(nombre)), random.choice(tipo), random.choice(debil))
    arbol_nombres = insertar_nodo(arbol_nombres, [pokemon, pokemon.nombre])
    arbol_tipo = insertar_nodo(arbol_tipo, [pokemon, pokemon.tipo])
    arbol_numero = insertar_nodo(arbol_numero, [pokemon, pokemon.numero])
def mainej2():
    eleccion = solicitar_introducir_numero_extremo("1. Mostrar los datos cargados\n2. Mostrar información del pokemon dado el número\n3. Mostrar pokemon dado el nombre por proximidad\n4. Mostrar todos los pokemon de un tipo\n5. Realizar un listado en orden ascendente por número de Pokémon\n6. Realizar un listado en orden ascendente por nombre de Pokémon\n7. Realizar un listado en orden ascendente por nivel por nombre\n8. Mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum\n9. Mostrar todos los tipos de Pokémons y cuántos hay de cada tipo.\n10. Salir", 1, 10)
    print("=" * 50)
    if eleccion == 1:
        print('Listado en orden por número:')
        inorden_numero(arbol_numero)
        print("=" * 50)
        mainej2()
    if eleccion == 2:
        numero = solicitar_introducir_numero_extremo("Introduzca el numero del pokemon", 1, len(nombre))
        print("Nombre: ", datos[numero][1]), print("Tipo: ", datos[numero][2])
        print("=" * 50)
        mainej2()
    elif eleccion == 3:
        busqueda_proximidad_poke(arbol_nombres, solicitar_introducir_cadena("Introduzca el nombre del pokemon: "))
        print("=" * 50)
        mainej2()
    elif eleccion == 4:
        tipo = solicitar_introducir_cadena('Ingrese el tipo de pokemon a buscar')
        print('Todos los pokemons de un tipo:')
        busqueda_proximidad_poke2(arbol_tipo, tipo.lower())
        print("=" * 50)
        mainej2()
    elif eleccion == 5:
        print('Listado en orden ascendente por número de Pokémon:')
        inorden_numero(arbol_numero)
        print("=" * 50)
        mainej2()
    elif eleccion == 6:
        print('Listado en orden ascendente por nombre de Pokémon:')
        inorden_nombre(arbol_nombres)
        print("=" * 50)
        mainej2()
    elif eleccion == 7:
        print('Listado en orden ascendente por nivel por nombre:')
        por_nivel_nombre(arbol_nombres)
        print("=" * 50)
        mainej2()
    elif eleccion == 8:
        print('Todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum:')
        busqueda_proximidad_poke3(arbol_tipo, 'Jolteon')
        busqueda_proximidad_poke3(arbol_tipo, 'Lycanroc')
        busqueda_proximidad_poke3(arbol_tipo, 'Tyrantrum')
        print("=" * 50)
        mainej2()
    elif eleccion == 9:
        print('Todos los tipos de Pokémons y cuántos hay de cada tipo:')
        cont = 0
        cont = inorden_tipo(arbol_nombres, cont)
        print('Cantidad del tipo fuego:',cont)
        print("=" * 50)
        mainej2()
    elif eleccion == 10:
        pass
```

<h2 align = "center"> Ejercicio 3: Siete maravillas</h2>

![image](https://user-images.githubusercontent.com/91721855/204055906-a2fa0a84-115d-436f-a80f-09227405d88e.png)
![image](https://user-images.githubusercontent.com/91721855/204056169-39a6df60-8e25-4880-a4a3-66985856e213.png)

El código empleado es el siguiente:

```python
from clases.grafo import Grafo
from introducir.numero import solicitar_introducir_numero_extremo

diccionario = [{'Nombre': 'Gran Pirámide de Guiza', 'País': 'Egipto', 'Tipo': 'Arquitectónica'},
{'Nombre': 'Jardines Colgantes de Babilonia', 'País': 'Irak', 'Tipo': 'Arquitectónica'},
{'Nombre': 'Templo de Artemisa', 'País': 'Turquía', 'Tipo': 'Arquitectónica'},
{'Nombre': 'Estatua de Zeus en Olimpia', 'País': 'Grecia', 'Tipo': 'Arquitectónica'},
{'Nombre': 'Mausoleo de Halicarnaso', 'País': 'Turquía', 'Tipo': 'Arquitectónica'},
{'Nombre': 'Coloso de Rodas', 'País': 'Grecia', 'Tipo': 'Arquitectónica'},
{'Nombre': 'Faro de Alejandría', 'País': 'Egipto', 'Tipo': 'Arquitectónica'},

{'Nombre': 'Cataratas de Iguazú', 'País': 'Argentina-Brasil-Paraguay', 'Tipo': 'Natural'},
{'Nombre': 'Montaña de Mesa', 'País': 'Sudáfrica', 'Tipo': 'Natural'},
{'Nombre': 'Amazonia', 'País': 'Brasil', 'Tipo': 'Natural'},
{'Nombre': 'Bahía de Ha-long', 'País': 'Vietnam', 'Tipo': 'Natural'},
{'Nombre': 'Isla Jeju', 'País': 'Corea del Sur', 'Tipo': 'Natural'},
{'Nombre': 'Parque Nacional de Komodo', 'País': 'Indonesia', 'Tipo': 'Natural'},
{'Nombre': 'Río Subterráneo de Puerto Princesa', 'País': 'Filipinas', 'Tipo': 'Natural'}]


g = Grafo(dirigido=False)

g.insertar_vertice('T', datos=diccionario[0])
g.insertar_vertice('Z', datos=diccionario[1])
g.insertar_vertice('F', datos=diccionario[2])
g.insertar_vertice('X', datos=diccionario[3])
g.insertar_vertice('R', datos=diccionario[4])
g.insertar_vertice('K', datos=diccionario[5])
g.insertar_vertice('S', datos=diccionario[6])
g.insertar_vertice('L', datos=diccionario[7])
g.insertar_vertice('J', datos=diccionario[8])
g.insertar_vertice('I', datos=diccionario[9])
g.insertar_vertice('M', datos=diccionario[10])
g.insertar_vertice('S', datos=diccionario[11])
g.insertar_vertice('Y', datos=diccionario[12])
g.insertar_vertice('H', datos=diccionario[13])


def mainej3():
    eleccion = solicitar_introducir_numero_extremo("1. Mostrar las maravillas\n2. Mostrar árbol de expansión mínimo\n3. Mostrar países con maravillas de los 2 tipos\n4. Mostrar los países con más de 1 maravilla del mismo tipo\n5. Salir", 1, 5)
    if eleccion == 1:
        print(diccionario)
        print("=" * 50)
        mainej3()
    elif eleccion == 2:
        print("El árbol de expansión mínimo de cada tipo de las maravillas es:")
        print("Arquitectónico:")
        print(Grafo.prim_minimo(g, "T"))
        print("Natural:")
        print(Grafo.prim_minimo(g, "L"))
        print("=" * 50)
        mainej3()
    elif eleccion == 3:
        print("Los países que disponen de maravillas arquitectónicas y naturales son:")
        for i in range(len(diccionario)):
            for j in range(len(diccionario)):
                if diccionario[i]['País'] == diccionario[j]['País'] and diccionario[i]['Tipo'] != diccionario[j]['Tipo']:
                    print(diccionario[i]['País'])
        print("Ninguno")
        print("=" * 50)
        mainej3()
    elif eleccion == 4:
        print("Los países que disponen de más de una maravilla del mismo tipo son:")
        for i in range(len(diccionario)):
            for j in range(len(diccionario)):
                if diccionario[i]['País'] == diccionario[j]['País'] and diccionario[i]['Tipo'] == diccionario[j]['Tipo'] and i != j:
                    print(diccionario[i]['País'])
        print("=" * 50)
        mainej3()
    elif eleccion == 5:
        pass
```

<h2 align = "center"> Lanzador </h2>

El código empleado es el siguiente:

```python
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
    eleccion = solicitar_introducir_numero_extremo("Introduzca el número del ejercicio que desea ejecutar:\n1. StarWars\n2. Pokémon\n3. Siete Maravillas\n4. Salir",1,4)
    print(Fore.RESET)
    if eleccion == 1:
        os.system('cls')
        print(Fore.LIGHTMAGENTA_EX +"Poe Dameron, líder del escuadrón negro de la Resistencia, tiene dificultades para transmitir los mensajes a la\nbase de la Resistencia, dado que los mismos son muy largos y los satélites espías de la Primera Orden los intercepta, en un\nlapso muy corto desde que se transmiten. Por lo cual, nos solicita desarrollar un algoritmo que permita comprimir los\nmensajes para enviarlos más rápido y no puedan ser interceptados. Contemplando los siguientes requerimientos, implementar\nun algoritmo que los resuelva:\na.crear un árbol de Huffman a partir de la siguiente tabla:\nb.desarrollar las funciones para comprimir y descomprimir un mensaje.\n", Fore.RESET)
        mainej1()
        main()
    elif eleccion == 2:
        os.system('cls')
        print(Fore.LIGHTMAGENTA_EX +"Se tiene un archivo con los Pokémons de las 8 generaciones cargados de manera desordenada (890 en total) de los\ncuales se conoce su nombre, número, tipo/tipos, debilidad frente a tipo/ tipos, para el cual debemos construir tres\nárboles para acceder de manera eficiente a los datos almacenados en el archivo, contemplando lo siguiente:\na.los índices de cada uno de los árboles deben ser nombre, número y tipo\nb.mostrar todos los datos de un Pokémon a partir de su número y nombre\n(para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar\ntodos los Pokémons cuyos nombres comiencen o contengan dichos caracteres)\nc.mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico.\nrealizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre.\nd.mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum.\ne.mostrar todos los tipos de Pokémons y cuántos hay de cada tipo.\n", Fore.RESET)
        mainej2()
        main()
    elif eleccion == 3:
        os.system('cls')
        print(Fore.LIGHTMAGENTA_EX +"Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas y naturales del mundo,\npara lo cual se deben tener en cuenta las siguientes actividades:\na.de cada una de las maravillas se conoce su nombre,país de ubicación (puede ser más de uno en las naturales) y tipo (natural o arquitectónica)\nb.cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar la distancia que las separa\nc.hallar el árbol de expansión mínimo de cada tipo de las maravillas.\nd. determinar si existen países que dispongan de maravillas arquitectónicas y naturales.\ne. determinar si algún país tiene más de una maravilla del mismo tipo.\nf. deberá utilizar un grafo no dirigido.)\n", Fore.RESET)
        mainej3()
        main()
    elif eleccion == 4:
        os.system('cls')
        exit()

if __name__ == '__main__':
    main()
```
