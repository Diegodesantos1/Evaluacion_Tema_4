from clases.cola import Cola
from clases.huffman import nodoArbolHuffman
class Ejercicio1:
    tabla_probabilidades = [['A', 0.2], ['F', 0.17], ['1', 0.13], ['3', 0.21], ['0', 0.05], ['M', 0.09], ['T', 0.15]]

    diccionario_convertido = {'A' : '00', '3': '01', '1' : '100', 'T': '110', 'F' : '111', '0': '1010', 'M' : '1011'}

    bosque = []

    for elemento in tabla_probabilidades:
        nodo = nodoArbolHuffman(elemento[0], elemento[1])
        bosque.append(nodo)

    for elemento in bosque:
        print(elemento.info, elemento.valor)
    while(len(bosque) > 1):
        elemento1 = bosque.pop(0)
        elemento2 = bosque.pop(0)
        nodo = nodoArbolHuffman('', elemento1.valor+elemento2.valor)
        nodo.izq = elemento1
        nodo.der = elemento2
        bosque.append(nodo)



