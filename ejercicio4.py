class Elemento:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad

    def __str__(self):
        return f"{self.nombre} (Prioridad: {self.prioridad})"

class ColaPrioridad:
    def __init__(self):
        self.cola = []

    def encolar(self, nombre, prioridad):
        nuevo = Elemento(nombre, prioridad)
        self.cola.append(nuevo)
        self.cola.sort(key=lambda x: x.prioridad)
        print(f"[ENCOLADO] {nuevo}")

    def desencolar(self):
        if self.cola:
            print(f"[DESENCOLADO] {self.cola.pop(0)}")
        else:
            print("[VACÍA] La cola está vacía.")

    def mostrar(self):
        if not self.cola:
            print("[VACÍA] Cola vacía.")
        else:
            print("\\n[COLA DE PRIORIDAD]")
            for i, e in enumerate(self.cola):
                print(f"{i + 1}. {e}")

def cola_prioridad_menu():
    cola = ColaPrioridad()
    while True:
        print("\\n--- Menú Cola de Prioridad ---")
        print("1. Encolar elemento")
        print("2. Desencolar")
        print("3. Mostrar cola")
        print("4. Volver al menú principal")
        opcion = input("Opción: ")
        if opcion == "1":
            nombre = input("Nombre: ")
            try:
                prioridad = int(input("Prioridad (entero, menor = mayor prioridad): "))
                cola.encolar(nombre, prioridad)
            except ValueError:
                print("[ERROR] Prioridad debe ser número entero.")
        elif opcion == "2":
            cola.desencolar()
        elif opcion == "3":
            cola.mostrar()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

