# Ejercicio 2: Verificar paréntesis balanceados
# Implementar una función que verifique si los paréntesis en una expresión están balanceados.
# La función debe recibir una cadena de texto y devolver True si están balanceados, False en caso contrario.
# Para esto se puede usar una pila.
# Se consideran los siguientes tipos de paréntesis: (), [], {}
def parentesis_balanceados(cadena):
    pila = []
    pares = {')': '(', ']': '[', '}': '{'}
    for caracter in cadena:
        if caracter in '([{':
            pila.append(caracter)
        elif caracter in ')]}':
            if not pila or pila[-1] != pares[caracter]:
                return False
            pila.pop()
    return not pila

def verificar_parentesis_menu():
    cadena = input("Ingrese una cadena para verificar paréntesis: ")
    if parentesis_balanceados(cadena):
        print("Paréntesis balanceados.")
    else:
        print("Paréntesis NO balanceados.")