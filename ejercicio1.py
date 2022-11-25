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

Ejercicio1.generar_tabla(Ejercicio1.bosque[0])

cadena_descodificar = int(input('Ingrese la cadena a decodificar en binario: '))
cadena_descodificar = str(cadena_descodificar)
cadena_codificar = input('Ingrese la cadena a codificar: ')
print('La cadena descodificada es: ', Ejercicio1.descodificar(cadena_descodificar, Ejercicio1.bosque[0]))
print('La cadena codificada es: ', Ejercicio1.codificar(cadena_codificar, Ejercicio1.diccionario_convertido))