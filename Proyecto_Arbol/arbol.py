class Nodo:
    """Clase que representa un nodo en un árbol binario de búsqueda."""
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def insertar(raiz, valor):
    """Inserta un nuevo valor en el árbol binario de búsqueda."""
    """Si el árbol está vacío, crea un nuevo nodo. Si no, inserta recursivamente."""
    if raiz is None:
        return Nodo(valor)
    if valor < raiz.valor:
        raiz.izq = insertar(raiz.izq, valor)
    else:
        raiz.der = insertar(raiz.der, valor)
    return raiz

def postorden(nodo):
    """Realiza un recorrido en postorden del árbol."""
    if nodo:
        postorden(nodo.izq)
        postorden(nodo.der)
        print(nodo.valor, end=' ')

def inorden(nodo):
    """Realiza un recorrido en inorden del árbol."""
    if nodo:
        inorden(nodo.izq)
        print(nodo.valor, end=' ')
        inorden(nodo.der)

def preorden(nodo):
    """Realiza un recorrido en preorden del árbol."""
    if nodo:
        print(nodo.valor, end=' ')
        preorden(nodo.izq)
        preorden(nodo.der)


