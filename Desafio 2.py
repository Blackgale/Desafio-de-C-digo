def remove_palavras_duplicadas(frase):
    palavras = frase.split()
    palavras_sem_duplicatas = []
    for palavra in palavras:
        if palavra not in palavras_sem_duplicatas:
            palavras_sem_duplicatas.append(palavra)
    nova_frase = ' '.join(palavras_sem_duplicatas)
    return nova_frase

frase_original = "Hello World!"
frase_sem_duplicatas = remove_palavras_duplicadas(frase_original)
print(frase_sem_duplicatas)