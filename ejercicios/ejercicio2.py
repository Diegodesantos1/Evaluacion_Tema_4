from clases.arbolbinario import insertar_nodo
from clases.cola import Cola, arribo, atencion, cola_vacia
import random
arbol_nombres = None
arbol_tipo = None
arbol_numero = None

class Pokemon(object):

    def __init__(self, nombre, numero, tipo, debilidad):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo
        self.debilidad = debilidad

    def __str__(self):
       return self.nombre + ' ' + str(self.numero) + ' ' + self.tipo + ' ' + self.debilidad

tipo = ['agua', 'fuego', 'tierra', 'electrico']
debil = ['agua', 'fuego', 'tierra', 'electrico', 'Jolteon', 'Lycanroc', 'Tyrantum']
nombre = ['Bulbasaur', 'Charmander', 'Pikachu', 'Ivysaur', 'Charmeleon', 'Charizard', 'Squirtle', 'wartortle', 'Venusaur']


for i in range (0, len(nombre)):
    pokemon = Pokemon(nombre[i], random.randint(1, 100), random.choice(tipo), random.choice(debil))
    arbol_nombres = insertar_nodo(arbol_nombres, [pokemon, pokemon.nombre])
    arbol_tipo = insertar_nodo(arbol_tipo, [pokemon, pokemon.tipo])
    arbol_numero = insertar_nodo(arbol_numero, [pokemon, pokemon.numero])

print("Apartado B")
def inorden_numero(raiz):
    if(raiz is not None):
        inorden_numero(raiz.izq)
        print(raiz.info[1], raiz.info[0])
        inorden_numero(raiz.der)
print('Listado en orden por número:')
inorden_numero(arbol_numero)
print()

def busqueda_proximidad_poke(raiz, buscado):
    if(raiz is not None):
        if(raiz.info[1][0:len(buscado)] == buscado):
            print(raiz.info[1])
        busqueda_proximidad_poke(raiz.izq, buscado)
        busqueda_proximidad_poke(raiz.der, buscado)

x = input('Ingrese el nombre parcial de pokemon a buscar:')
print('Todos los pokemons con ese nombre parcial:')
busqueda_proximidad_poke(arbol_nombres, x)
print()

print("Apartado C")
def busqueda_proximidad_poke2(raiz, buscado):
    if(raiz is not None):
        if(raiz.info[1][0:len(buscado)] == buscado):
            print(raiz.info[0].nombre)
        busqueda_proximidad_poke2(raiz.izq, buscado)
        busqueda_proximidad_poke2(raiz.der, buscado)

x = input('Ingrese el tipo de pokemon a buscar:')
print('Todos los pokemons de un tipo:')
busqueda_proximidad_poke2(arbol_tipo, x.lower())
print()

print("Apartado D")
def inorden_numero2(raiz):
    if(raiz is not None):
        inorden_numero2(raiz.izq)
        print(raiz.info[0])
        inorden_numero2(raiz.der)

print('Listado en orden creciente numérico de pokemons:')
inorden_numero2(arbol_numero)
print()

def inorden_nombre(raiz):
    if(raiz is not None):
        inorden_nombre(raiz.izq)
        print(raiz.info[0])
        inorden_nombre(raiz.der)

print('Listado en orden creciente alfabético de pokemons:')
inorden_nombre(arbol_nombres)
print()

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

print('Listado en orden por nivel de pokemons:')
por_nivel_nombre(arbol_nombres)
print()

print("Apartado E")
def busqueda_proximidad_poke3(raiz, buscado):
    if(raiz is not None):
        if(raiz.info[0].debilidad[0:len(buscado)] == buscado):
            print(raiz.info[0].nombre)
        busqueda_proximidad_poke3(raiz.izq, buscado)
        busqueda_proximidad_poke3(raiz.der, buscado)

print('Debiles contra Jolteon: ')
busqueda_proximidad_poke3(arbol_nombres, 'Jolteon')
print()

print('Debiles contra Lycanroc: ')
busqueda_proximidad_poke3(arbol_nombres, 'Lycanroc')
print()

print('Debiles contra Tyrantrum: ')
busqueda_proximidad_poke3(arbol_nombres, 'Tyrantrum')
print()

print("Apartado F")
cont = 0

def inorden_tipo(raiz, cont):
    if(raiz is not None):
        if raiz.info[0].tipo == 'fuego':
            cont += 1
        inorden_tipo(raiz.izq, cont)
        print(raiz.info[0].nombre, raiz.info[0].tipo)
        inorden_tipo(raiz.der, cont)
    return cont

print('Pokemons y su tipo:')
cont = inorden_tipo(arbol_nombres, cont)
print()

print('Cantidad del tipo fuego:',cont)
