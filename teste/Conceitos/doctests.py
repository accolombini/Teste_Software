"""
Doctests => seu teste serve de documentação para seu código -> faz uso das conhecidas Docstrings. Vale a pena aprender, mas não recomendo o uso.

    - Para usar Docstrings como teste, você deve reproduzir exatamente o ambiente de desenvolvimento do seu termina Python incluindo o prompt >>>
    - Para rodar seu teste utilizando Doctests use o comando a seguir no seu terminal:
        python -m doctest -v <nome_do_seu_codigo.py>
    - Observe a saída de um teste com Doctests
            (teste_software) ➜  Conceitos git:(main) ✗ python -m doctest -v doctests.py
                Trying:
                    soma(1, 2)
                Expecting:
                    3
                ok
                Trying:
                    soma(4, -9)
                Expecting:
                    13
                **********************************************************************
                File "/Users/accol/Library/CloudStorage/OneDrive-Pessoal/TESTES/T_Software_Python/teste/Conceitos/doctests.py", line 15, in doctests.soma
                Failed example:
                    soma(4, -9)
                Expected:
                    13
                Got:
                    -5
                1 items had no tests:
                doctests
                **********************************************************************
                1 items had failures:
                1 of   2 in doctests.soma
                2 tests in 2 items.
                1 passed and 1 failed.
                ***Test Failed*** 1 failures.
    
"""


def soma(a, b):
    """Soma os números a e b
    >>> soma(1, 2)
    3
    >>> soma(4, -9)
    13
    """
    return a + b


# Fazendo uso de teste manual -> teste de mesa
pri = int(input('Entre com o valor do primeiro número: '))
seg = int(input('Entre com o valor do segundo número: '))
print(f'Fazendo uso de Doctestes => {soma(pri, seg)}')
