"""
Este é um laboratório com foco no UNITTEST.

    |> O que será a prática baconcomovos:
        - Receber um número inteiro
        - Saber se o número é múltiplo de 3 e 5
            Se verdade -> retornar Bacon com ovos
        - Saber se o número é múltiplo somente de 3
            Se verdade -> retorne Bacon
        - Saber se o número é múltiplo somente de 5
            Se verdade -> retornar Ovos
        - Saber se o número não é múltiplo de 3 e de 5
            Se verdade -> retornar 'Passa fome'

"""

# Criando a função bacon_com_ovos para atender erro 1


def bacon_com_ovos(n):  # Passo 1, criando apenas para passar no teste
    assert isinstance(n, int), f"n deve ser int! Você digitou -> {type(n)}"

    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com ovos'

    if n % 3 == 0:
        return 'Bacon'

    if n % 5 == 0:
        return 'Ovos'

    return 'Passar fome'
