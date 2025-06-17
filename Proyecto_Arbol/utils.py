def dibujar_arbol(nodo, prefijo="", es_izq=True):
    """Dibuja el árbol binario de búsqueda de forma visual (de arriba hacia abajo)."""
    if nodo is not None:
        if nodo.der:
            dibujar_arbol(nodo.der, prefijo + "    ", False)
        print(prefijo + ("└── " if es_izq else "┌── ") + str(nodo.valor))
        if nodo.izq:
            dibujar_arbol(nodo.izq, prefijo + "    ", True)


def validar_entrada(entrada):
    """Valida la entrada del usuario y convierte los valores a enteros."""
    valores = []
    for v in entrada.split(","):
        v = v.strip()
        if v.isdigit() or (v.startswith('-') and v[1:].isdigit()):
            valores.append(int(v))
        else:
            print(f"Advertencia: '{v}' no es un número válido y será ignorado.")
    return valores