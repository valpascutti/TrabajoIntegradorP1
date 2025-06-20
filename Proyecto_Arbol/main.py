from arbol import insertar, postorden, inorden, preorden
from utils import dibujar_arbol, validar_entrada

# Programa principal.
def main():
    """Función principal que solicita al usuario los valores del árbol y ejecuta las operaciones."""
    print("Bienvenido al programa de Árbol Binario de Búsqueda.")

    while True:
        entrada = input("Ingresá los valores del árbol separados por comas (ej: 8,3,10,1,6): ")
        if not entrada.strip():
            print("Entrada vacía. Por favor, ingresá al menos un valor.")
            continue

        valores = validar_entrada(entrada)
        if not valores:
            print("No se ingresaron valores válidos.")
            exit()

        raiz = None
        for v in valores:
           raiz = insertar(raiz, v)

        print("\nElegí el recorrido que prefieras:")
        print("1. Postorden")
        print("2. Inorden")
        print("3. Preorden")
        opcion = input("Opción: ")

        if opcion == "1":
         postorden(raiz)
        elif opcion == "2":
         inorden(raiz)
        elif opcion == "3":
         preorden(raiz)
        else:
            print("Opción no válida.")

        print("\n\nÁrbol binario representado visualmente:")
        dibujar_arbol(raiz)

        continuar = input("\n¿Deseás crear otro árbol? (s/n): ").strip().lower()
        if continuar != 's':
            print("¡Gracias por usar el programa!")
            break

if __name__ == "__main__":
    main()