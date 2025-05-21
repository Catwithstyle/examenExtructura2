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