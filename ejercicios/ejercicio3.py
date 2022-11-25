from clases.grafo import Grafo

diccionario = {'Nombre': 'Río Subterráneo de Puerto Princesa', 'País': 'Filipinas', 'Tipo': 'Natural'}

g = Grafo(dirigido=False)

g.insertar_vertice('T', datos={'Nombre': 'Gran Pirámide de Guiza', 'País': 'Egipto', 'Tipo': 'Arquitectónica'})
g.insertar_vertice('Z', datos={'Nombre': 'Jardines Colgantes de Babilonia', 'País': 'Irak', 'Tipo': 'Arquitectónica'})
g.insertar_vertice('F', datos={'Nombre': 'Templo de Artemisa', 'País': 'Turquía', 'Tipo': 'Arquitectónica'})
g.insertar_vertice('X', datos={'Nombre': 'Estatua de Zeus en Olimpia', 'País': 'Grecia', 'Tipo': 'Arquitectónica'})
g.insertar_vertice('R', datos={'Nombre': 'Mausoleo de Halicarnaso', 'País': 'Turquía', 'Tipo': 'Arquitectónica'})
g.insertar_vertice('K', datos={'Nombre': 'Coloso de Rodas', 'País': 'Grecia', 'Tipo': 'Arquitectónica'})
g.insertar_vertice('S', datos={'Nombre': 'Faro de Alejandría', 'País': 'Egipto', 'Tipo': 'Arquitectónica'})

g.insertar_vertice('L', datos={'Nombre': 'Cataratas de Iguazú', 'País': 'Argentina-Brasil-Paraguay', 'Tipo': 'Natural'})
g.insertar_vertice('J', datos={'Nombre': 'Montaña de Mesa', 'País': 'Sudáfrica', 'Tipo': 'Natural'})
g.insertar_vertice('I', datos={'Nombre': 'Amazonia', 'País': 'Brasil', 'Tipo': 'Natural'})
g.insertar_vertice('M', datos={'Nombre': 'Bahía de Ha-long', 'País': 'Vietnam', 'Tipo': 'Natural'})
g.insertar_vertice('S', datos={'Nombre': 'Isla Jeju', 'País': 'Corea del Sur', 'Tipo': 'Natural'})
g.insertar_vertice('Y', datos={'Nombre': 'Parque Nacional de Komodo', 'País': 'Indonesia', 'Tipo': 'Natural'})
g.insertar_vertice('H', datos={'Nombre': 'Río Subterráneo de Puerto Princesa', 'País': 'Filipinas', 'Tipo': 'Natural'})


def mainej3():

    print("El árbol de expansión mínimo de cada tipo de las maravillas es:")
    print("Arquitectónico:")
    print(Grafo.prim_minimo(g, "T"))
    print("Natural:")
    print(Grafo.prim_minimo(g, "L"))