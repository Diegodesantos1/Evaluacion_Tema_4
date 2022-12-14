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


tipo = ['agua', 'fuego', 'tierra', 'electrico', 'planta', 'hada', 'volador', 'dragon',
        'fantasma', 'siniestro', 'lucha', 'roca', 'psiquico', 'bicho', 'normal', 'veneno', 'acero']
debil = ['agua', 'fuego', 'tierra', 'electrico',
         'planta', 'Jolteon', 'Lycanroc', 'Tyrantum']


for i in range(0, len(nombre)):
    pokemon = Pokemon(nombre[i], random.randint(
        1, len(nombre)), random.choice(tipo), random.choice(debil))
    arbol_nombres = insertar_nodo(arbol_nombres, [pokemon, pokemon.nombre])
    arbol_tipo = insertar_nodo(arbol_tipo, [pokemon, pokemon.tipo])
    arbol_numero = insertar_nodo(arbol_numero, [pokemon, pokemon.numero])


def mainej2():
    eleccion = solicitar_introducir_numero_extremo("1. Mostrar los datos cargados\n2. Mostrar informaci??n del pokemon dado el n??mero\n3. Mostrar pokemon dado el nombre por proximidad\n4. Mostrar todos los pokemon de un tipo\n5. Realizar un listado en orden ascendente por n??mero de Pok??mon\n6. Realizar un listado en orden ascendente por nombre de Pok??mon\n7. Realizar un listado en orden ascendente por nivel por nombre\n8. Mostrar todos los Pok??mons que son d??biles frente a Jolteon, Lycanroc y Tyrantrum\n9. Mostrar todos los tipos de Pok??mons y cu??ntos hay de cada tipo.\n10. Salir", 1, 10)
    print("=" * 50)
    if eleccion == 1:
        print('Listado en orden por n??mero:')
        inorden_numero(arbol_numero)
        print("=" * 50)
        mainej2()
    if eleccion == 2:
        numero = solicitar_introducir_numero_extremo(
            "Introduzca el numero del pokemon", 1, len(nombre))
        print("Nombre: ", datos[numero][1]), print("Tipo: ", datos[numero][2])
        print("=" * 50)
        mainej2()
    elif eleccion == 3:
        busqueda_proximidad_poke(arbol_nombres, solicitar_introducir_cadena(
            "Introduzca el nombre del pokemon: "))
        print("=" * 50)
        mainej2()
    elif eleccion == 4:
        tipo = solicitar_introducir_cadena(
            'Ingrese el tipo de pokemon a buscar')
        print('Todos los pokemons de un tipo:')
        busqueda_proximidad_poke2(arbol_tipo, tipo.lower())
        print("=" * 50)
        mainej2()
    elif eleccion == 5:
        print('Listado en orden ascendente por n??mero de Pok??mon:')
        inorden_numero(arbol_numero)
        print("=" * 50)
        mainej2()
    elif eleccion == 6:
        print('Listado en orden ascendente por nombre de Pok??mon:')
        inorden_nombre(arbol_nombres)
        print("=" * 50)
        mainej2()
    elif eleccion == 7:
        print('Listado en orden ascendente por nivel por nombre:')
        por_nivel_nombre(arbol_nombres)
        print("=" * 50)
        mainej2()
    elif eleccion == 8:
        print('Todos los Pok??mons que son d??biles frente a Jolteon, Lycanroc y Tyrantrum:')
        busqueda_proximidad_poke3(arbol_tipo, 'Jolteon')
        busqueda_proximidad_poke3(arbol_tipo, 'Lycanroc')
        busqueda_proximidad_poke3(arbol_tipo, 'Tyrantrum')
        print("=" * 50)
        mainej2()
    elif eleccion == 9:
        print('Todos los tipos de Pok??mons y cu??ntos hay de cada tipo:')
        cont = 0
        cont = inorden_tipo(arbol_nombres, cont)
        print('Cantidad del tipo fuego:', cont)
        print("=" * 50)
        mainej2()
    elif eleccion == 10:
        pass
