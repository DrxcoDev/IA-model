import numpy as np
import nltk 

# Descargar los recursos necesarios
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize 

def tokenize(text):
    tokens = word_tokenize(text)  # Tokenizamos el texto
    print("Tokens:", tokens)  # Mostramos los tokens generados

bible = {
    "good": ["almendras", "cebolla", "patatas", "lechuga", "tomate", "cheese"],
    "medium": ["leche", "picante", "pollo", "fish"],
    "worst": ["cookies", "pizza", "burguer", "donut"]
}

def calcular_porcentaje(coincidencia, palabra):
    return (coincidencia / len(palabra)) * 100 if len(palabra) > 0 else 0

def multi(x: int, y: int, dich: int = 1, prompt=None, abdupt=False):
    if dich == 0:
        print("El parámetro 'dich' no puede ser 0.")
        return

    if prompt is None:
        prompt = ""

    if x > 0:
        total_porcentaje = 0
        total_palabras = 0
        for j in prompt.split():
            found = False
            for category, words in bible.items():
                for word in words:
                    coincidencia = 0
                    for k in range(min(len(j), len(word))):
                        if j[k].lower() == word[k].lower():
                            coincidencia += 1

                    porcentaje = calcular_porcentaje(coincidencia, word)
                    
                    if porcentaje > 0:
                        print(f"Coincidencia parcial de '{j}' con '{word}' en la categoría '{category}' ({porcentaje:.2f}%)")
                        total_porcentaje += porcentaje
                        total_palabras += 1
                        found = True
                        break

            if not found:
                print(f"No se encontró '{j}' en las categorías de 'bible'.")

        if total_palabras > 0:
            porcentaje_promedio = total_porcentaje / total_palabras
            print("{", f"{porcentaje_promedio:.2f}%", "} De coincidencias")

        if abdupt:
            for i in range(1, y + 1):
                result = (x * np.pi + i) / dich
                print(f"{result:.4f}")
        
        tokenize(prompt)  # Llamamos a la función tokenize después de procesar las palabras
    else:
        print(f"{x} es menor a 0")

