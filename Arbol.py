from collections import deque

class Arbol:
    def __init__(self, elemento):
        self.hijos = []
        self.elemento = elemento
    def agregarElemento(arbol, elemento, elementoPadre):
        subarbol = arbol.buscarSubarbol(arbol, elementoPadre);
        subarbol.hijos.append(Arbol(elemento))

    def buscarSubarbol(arbol, elemento):
        if arbol.elemento == elemento:
            return arbol
        for subarbol in arbol.hijos:
            arbolBuscado = arbol.buscarSubarbol(subarbol, elemento)
        if (arbolBuscado != None):
            return arbolBuscado
        return None
    def profundidad(arbol):
        if len(arbol.hijos) == 0:
            return 1
        return 1 + max(map(arbol.profundidad,arbol.hijos))

    def grado(arbol):
        return max(map(grado, arbol.hijos) + [len(arbol.hijos)])
    def ejecutarProfundidadPrimero(arbol, funcion):
        funcion(arbol.elemento)
        for hijo in arbol.hijos:
            arbol.ejecutarProfundidadPrimero(hijo, funcion)

    def ejecutarAnchoPrimero(arbol, funcion, cola = deque()):
        funcion(arbol.elemento)
        if (len(arbol.hijos) > 0):
            cola.extend(arbol.hijos)
        if (len(cola) != 0):
            arbol.ejecutarAnchoPrimero(cola.popleft(), funcion, cola)




