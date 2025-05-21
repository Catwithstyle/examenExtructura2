#Ejercicio 1: Invertir palabras de una frase
# Implementar una función que invierta el orden de las palabras en una frase utilizando una pila.
# La función debe recibir una cadena de texto y devolver la cadena con las palabras en orden inverso.
def invertir_frase(frase):
    pila = []
    palabras = frase.split()
    for palabra in palabras:
        pila.append(palabra)
    frase_invertida = ""
    while pila:
        frase_invertida += pila.pop() + " "
    return frase_invertida.strip()

def invertir_palabras_menu():
    frase = input("Ingrese una frase: ")
    resultado = invertir_frase(frase)
    print("Frase invertida:", resultado)