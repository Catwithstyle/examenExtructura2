class Cancion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.anterior = None
        self.siguiente = None

class ListaReproduccion:
    def __init__(self):
        self.actual = None

    def agregar_cancion(self, nombre):
        nueva = Cancion(nombre)
        if not self.actual:
            self.actual = nueva
        else:
            temp = self.actual
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nueva
            nueva.anterior = temp
        print(f"[AGREGADO] '{nombre}' a la lista.")

    def eliminar_cancion(self, nombre):
        temp = self.actual
        while temp:
            if temp.nombre == nombre:
                if temp.anterior:
                    temp.anterior.siguiente = temp.siguiente
                if temp.siguiente:
                    temp.siguiente.anterior = temp.anterior
                if temp == self.actual:
                    self.actual = temp.siguiente if temp.siguiente else temp.anterior
                print(f"[ELIMINADO] '{nombre}' eliminada.")
                return
            temp = temp.siguiente
        print(f"[NO ENCONTRADA] '{nombre}' no está en la lista.")

    def reproducir_siguiente(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            print(f"[REPRODUCIENDO] {self.actual.nombre}")
        else:
            print("[FIN] No hay más canciones.")

    def reproducir_anterior(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            print(f"[REPRODUCIENDO] {self.actual.nombre}")
        else:
            print("[INICIO] No hay canciones anteriores.")

    def mostrar_lista(self):
        temp = self.actual
        if not temp:
            print("[VACÍA] Lista vacía.")
            return
        while temp.anterior:
            temp = temp.anterior
        print("\\n[LISTA DE REPRODUCCIÓN]")
        while temp:
            marcador = "▶️" if temp == self.actual else "   "
            print(f"{marcador} {temp.nombre}")
            temp = temp.siguiente

def lista_reproduccion_menu():
    lista = ListaReproduccion()
    while True:
        print("\\n--- Menú Lista Reproducción ---")
        print("1. Agregar canción")
        print("2. Eliminar canción")
        print("3. Reproducir siguiente")
        print("4. Reproducir anterior")
        print("5. Mostrar lista")
        print("6. Volver al menú principal")
        opcion = input("Opción: ")
        if opcion == "1":
            lista.agregar_cancion(input("Nombre canción: "))
        elif opcion == "2":
            lista.eliminar_cancion(input("Nombre canción a eliminar: "))
        elif opcion == "3":
            lista.reproducir_siguiente()
        elif opcion == "4":
            lista.reproducir_anterior()
        elif opcion == "5":
            lista.mostrar_lista()
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")
