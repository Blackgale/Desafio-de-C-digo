###Para o primeiro desafio, teremos que criar uma função para nos ajudar. 
def inverter_ordem_palavras(frase):
    palavras = frase.split()
    palavras_invertidas = palavras[::-1]
    frase_invertida = ' '.join(palavras_invertidas)
    return frase_invertida

frase = "Hello World! OpenAI is amazing"
frase_invertida = inverter_ordem_palavras(frase)
print(frase_invertida)


###Caso de teste
def test_inverter_ordem_palavras():
    assert inverter_ordem_palavras("Palmeiras não tem Mundial") == "Mundial tem não Palmeiras" 
    assert inverter_ordem_palavras("Um Dois Três Quatro Cinco") == "Cinco Quatro Três Dois Um"
    assert inverter_ordem_palavras("A B C D E ") == "E D C B A"
    assert inverter_ordem_palavras("Eu amo gatos") == "gatos amo Eu"
    print("Todos os testes passaram.")

test_inverter_ordem_palavras()
