def primeira_letra_maiuscula(frase):
    frase_capitalizada = frase.title()
    return frase_capitalizada

frase_original = "hello, how are you? i'm fine, thank you."
frase_capitalizada = primeira_letra_maiuscula(frase_original)
print(frase_capitalizada)
