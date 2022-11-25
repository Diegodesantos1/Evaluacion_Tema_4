from clases.grafo import Grafo

diccionario = [{'Nombre': 'Gran Pirámide de Guiza', 'País': 'Egipto', 'Tipo': 'Arquitectónica'},{'Nombre': 'Jardines Colgantes de Babilonia', 'País': 'Irak', 'Tipo': 'Arquitectónica'},
{'Nombre': 'Templo de Artemisa', 'País': 'Turquía', 'Tipo': 'Arquitectónica'},{'Nombre': 'Estatua de Zeus en Olimpia', 'País': 'Grecia', 'Tipo': 'Arquitectónica'},
{'Nombre': 'Mausoleo de Halicarnaso', 'País': 'Turquía', 'Tipo': 'Arquitectónica'},{'Nombre': 'Coloso de Rodas', 'País': 'Grecia', 'Tipo': 'Arquitectónica'},
{'Nombre': 'Faro de Alejandría', 'País': 'Egipto', 'Tipo': 'Arquitectónica'},{'Nombre': 'Cataratas de Iguazú', 'País': 'Argentina-Brasil-Paraguay', 'Tipo': 'Natural'},
{'Nombre': 'Montaña de Mesa', 'País': 'Sudáfrica', 'Tipo': 'Natural'},{'Nombre': 'Amazonia', 'País': 'Brasil', 'Tipo': 'Natural'},{'Nombre': 'Bahía de Ha-long', 'País': 'Vietnam', 'Tipo': 'Natural'},
{'Nombre': 'Isla Jeju', 'País': 'Corea del Sur', 'Tipo': 'Natural'},{'Nombre': 'Parque Nacional de Komodo', 'País': 'Indonesia', 'Tipo': 'Natural'},
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
    print ("Apartado A")
    print(diccionario)
    print("El árbol de expansión mínimo de cada tipo de las maravillas es:")
    print("Arquitectónico:")
    print(Grafo.prim_minimo(g, "T"))
    print("Natural:")
    print(Grafo.prim_minimo(g, "L"))