def maior_substring_palindroma(s):
    max_tamanho = 0
    indice_inicio = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if substring == substring[::-1]:
                if len(substring) > max_tamanho:
                    max_tamanho = len(substring)
                    indice_inicio = i

    return s[indice_inicio:indice_inicio+max_tamanho]

string_entrada = "babad"
string_saida = maior_substring_palindroma(string_entrada)
print(string_saida)

###Caso de Teste
def test_maior_substring_palindroma():
    assert maior_substring_palindroma("babad") == "bab"
    assert maior_substring_palindroma("cbbd") == "bb"
    assert maior_substring_palindroma("a") == "a"
    assert maior_substring_palindroma("ac") == "a"
    assert maior_substring_palindroma("banana") == "anana"
    assert maior_substring_palindroma("abacdfgdcaba") == "aba"
    print("Todos os testes passaram.")

test_maior_substring_palindroma()
