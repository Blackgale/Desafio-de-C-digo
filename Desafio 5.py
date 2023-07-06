def anagrama_de_palindromo(s):
    frequencias = {}
    for caractere in s:
        if caractere in frequencias:
            frequencias[caractere] += 1
        else:
            frequencias[caractere] = 1

    impares = 0
    for frequencia in frequencias.values():
        if frequencia % 2 == 1:
            impares += 1

    return impares <= 1

input_string = "racecar"
output = anagrama_de_palindromo(input_string)
print(output)

##Caso de Teste
def teste_anagrama_de_palindromo():
    assert anagrama_de_palindromo("racecar") == True
    assert anagrama_de_palindromo("foobar") == False
    assert anagrama_de_palindromo("aabbcc") == True
    assert anagrama_de_palindromo("abcabc") == True
    assert anagrama_de_palindromo("abccba") == True
    print("Todos os testes passaram.")

teste_anagrama_de_palindromo()
