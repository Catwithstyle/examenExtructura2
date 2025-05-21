from ejercicio1 import invertir_palabras_menu
from ejercicio2 import verificar_parentesis_menu
from ejercicio3 import lista_reproduccion_menu
from ejercicio4 import cola_prioridad_menu
from ejercicio5 import lista_enlazada_busqueda_menu

def menu_principal():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Ejercicio 1: Invertir palabras con pila")
        print("2. Ejercicio 2: Verificar paréntesis balanceados")
        print("3. Ejercicio 3: Lista de reproducción con lista enlazada")
        print("4. Ejercicio 4: Cola de prioridad")
        print("5. Ejercicio 5: Búsqueda en lista enlazada")
        print("6. Salir")

        opcion = input("Seleccione un ejercicio: ")

        if opcion == "1":
            invertir_palabras_menu()
        elif opcion == "2":
            verificar_parentesis_menu()
        elif opcion == "3":
            lista_reproduccion_menu()
        elif opcion == "4":
            cola_prioridad_menu()
        elif opcion == "5":
            lista_enlazada_busqueda_menu()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
