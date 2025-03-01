import numpy as np
import nltk
import matplotlib.pyplot as plt
from flask import Flask, send_file
from nltk.tokenize import word_tokenize

# Descargar los recursos necesarios
nltk.download('punkt')
nltk.download('punkt_tab')

# Crear la aplicación de Flask
app = Flask(__name__)

# Función para tokenizar el texto
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

def multi(x: int, y: int, dich: int = 1, prompt=None, abdupt=False, graph=1, in_web=False):
    if dich == 0:
        print("El parámetro 'dich' no puede ser 0.")
        return

    if prompt is None:
        prompt = ""

    if x > 0:
        total_porcentaje = 0
        total_palabras = 0
        coincidencias = []
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

                        coincidencias.append((j, porcentaje))
                        break



            if not found:
                print(f"No se encontró '{j}' en las categorías de 'bible'.")

        if total_palabras > 0:
            porcentaje_promedio = total_porcentaje / total_palabras
            print("{", f"{porcentaje_promedio:.2f}%", "} De coincidencias")

        if graph == 2 and coincidencias:
            # Extraer datos para el gráfico
            words, percentages = zip(*coincidencias)
            
            fig, ax = plt.subplots()
            bars = ax.bar(words, percentages, color='blue', alpha=0.7)

            ax.set_xlabel("Palabras")
            ax.set_ylabel("Porcentaje de Coincidencia")
            ax.set_title("Coincidencia de palabras con categorías")

            # Agregar los valores sobre cada barra
            for bar, percent in zip(bars, percentages):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2, height, f'{percent:.2f}%', 
                        ha='center', va='bottom', fontsize=10, color='black', fontweight='bold')

            # Mostrar porcentaje promedio en el gráfico
            ax.text(0.5, 0.9, f'Promedio: {porcentaje_promedio:.2f}%', 
                    ha='center', va='top', transform=ax.transAxes, fontsize=12, color='red')

            plt.xticks(rotation=45)
            plt.grid(axis="y", linestyle="--", alpha=0.7)

            # Guardar el gráfico
            plt.savefig('gráfico.png')
            plt.show()  # Muestra el gráfico en pantalla

        if abdupt:
            for i in range(1, y + 1):
                result = (x * np.pi + i) / dich
                print(f"{result:.4f}")

        
        if in_web == True:
            # Crear una ruta para servir el gráfico
            @app.route('/')
            def home():
                return """
                <h1>Gráfico Generado</h1>
                <p>Haz clic en el siguiente enlace para ver el gráfico:</p>
                <a href="/plot">Ver gráfico</a>
                """

            # Crear una ruta para mostrar el gráfico
            @app.route('/plot')
            def plot():
                return send_file('gráfico.png', mimetype='image/png')

        tokenize(prompt)  # Llamamos a la función tokenize después de procesar las palabras
    else:
        print(f"{x} es menor a 0")



# Ejecutar el servidor
if __name__ == "__main__":
    size = 5
    large = 6
    dich = 2
    multi(size, large, dich, "Pizza con burguer", abdupt=True, graph=2, in_web=False)
    
