###Para o primeiro desafio, teremos que criar uma função para nos ajudar. 

def inverter_ordem_palavras(frase):
    palavras = frase.split()
    palavras_invertidas = palavras[::-1]
    frase_invertida = ' '.join(palavras_invertidas)
    return frase_invertida

frase = "Hello World! OpenAI is amazing"
frase_invertida = inverter_ordem_palavras(frase)
print(frase_invertida)
