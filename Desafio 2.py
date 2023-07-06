###Para o Desafio 2 usei basicamente a mesma estrutura do 1, só que pra isso em Nova Frase armazenei de forma vazia para que ele pudesse capturar isso.

def remove_caracteres_duplicados(frase):
    nova_frase = ''
    for caractere in frase:
        if caractere not in nova_frase:
            nova_frase += caractere
    return nova_frase

frase_original = "Hello World!"
frase_sem_duplicatas = remove_caracteres_duplicados(frase_original)
print(frase_sem_duplicatas)


###Caso de Teste
def teste_remove_caracteres_duplicados():
    assert remove_caracteres_duplicados("Hello World!") == "Helo Wrd!"
    assert remove_caracteres_duplicados("Cachorro Quente") == "Cahor Quent"
    assert remove_caracteres_duplicados("abcde") == "abcde"
    print("Todos os testes passaram.")

teste_remove_caracteres_duplicados()

