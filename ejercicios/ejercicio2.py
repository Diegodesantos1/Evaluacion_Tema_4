from clases.arbolbinario import insertar_nodo
from clases.cola import Cola, arribo, atencion, cola_vacia
from introducir.numero import solicitar_introducir_numero_extremo
import time
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
    eleccion = solicitar_introducir_numero_extremo("1. Mostrar información del pokemon dado el número\n2. Mostrar pokemon dado el nombre por proximidad\n3. Mostrar todos los pokemon de un tipo\n4. Buscar por debilidad\n5. Salir", 1, 5)
    if eleccion == 1:
        numero = solicitar_introducir_numero_extremo("Introduzca el numero del pokemon", 1, len(nombre))
        print("Nombre: ", datos[numero][1]), print("Tipo: ", datos[numero][2]), print("Debilidad: ", datos[numero][3])
    elif eleccion == 2:
        busqueda_proximidad_poke(arbol_nombres, str(input("Introduzca el nombre del pokemon: ")))
    elif eleccion == 3:
        tipo = str(input('Ingrese el tipo de pokemon a buscar:'))
        print('Todos los pokemons de un tipo:')
        busqueda_proximidad_poke2(arbol_tipo, tipo.lower())