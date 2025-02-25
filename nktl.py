import nltk 

# Descargar el tokenizer punkt y punkt_tab
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize 

# Texto a tokenizar
texto = "La tokenización de texto en Python es esencial para el procesamiento del lenguaje natural." 

# Tokenización
tokens = word_tokenize(texto) 

# Mostrar los tokens
print(tokens)
