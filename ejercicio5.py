# Ejercicio 5: Búsqueda en lista enlazada
# Implementar una lista enlazada que permita agregar elementos y buscar un elemento específico.
# La lista debe permitir mostrar todos los elementos en la lista.
# Se debe implementar una clase Nodo y una clase ListaEnlazada.
# Se debe implementar un menú para interactuar con la lista enlazada.
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
        print(f"[AGREGADO] {valor}")

    def buscar(self, valor):
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.valor == valor:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1

    def mostrar(self):
        actual = self.cabeza
        if not actual:
            print("[VACÍA] Lista vacía.")
            return
        print("\\n[LISTA ENLAZADA]")
        pos = 0
        while actual:
            print(f"{pos}. {actual.valor}")
            actual = actual.siguiente
            pos += 1

def lista_enlazada_busqueda_menu():
    lista = ListaEnlazada()
    while True:
        print("\\n--- Menú Lista Enlazada ---")
        print("1. Agregar valor")
        print("2. Buscar valor")
        print("3. Mostrar lista")
        print("4. Volver al menú principal")
        opcion = input("Opción: ")
        if opcion == "1":
            lista.agregar(input("Valor a agregar: "))
        elif opcion == "2":
            valor = input("Valor a buscar: ")
            pos = lista.buscar(valor)
            if pos != -1:
                print(f"[ENCONTRADO] '{valor}' está en la posición {pos}.")
            else:
                print(f"[NO ENCONTRADO] '{valor}' no está en la lista.")
        elif opcion == "3":
            lista.mostrar()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
