"""
Assertions (Afirmações/Checagens/Questionamentos)
Em Python utilizamos a palavra reservada 'assert' para realizar simples afirmações utilizadas nos testes.
Utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não. Se a expressão for verdadeira, retorna None e caso seja falsa levanta um erro do tipo AssertionError.
    Obs.: podemos especificar, opcionalmente, um segundo arqgumento ou mesmo uma mensagem de erro personalizada para fácil identificação e rastreio do erro.
    A palavra 'assert' pode ser utilizada em qualquer fução ou código que estajamos trabalhando, não precisa ser exclusivamente nos testes.
    
        (teste_software) ➜  T_Software_Python git:(main) ✗ python
        Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
        Type "help", "copyright", "credits" or "license" for more information.
        >>> assert 4 == 4
        >>> assert 4 == 5
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        AssertionError
        >>> assert 4 == 5, '4 é diferente de 5'
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        AssertionError: 4 é diferente de 5
        
ALERTA: Cuidado ao utilizar o 'assert'.....
    - Se um programa Python for executado com o parâmetro -O, nenhum assertion será validado. Ou seja, todas as suas validações já eram ....
    - Como exemplo faça => python -O assertions.py
    - Para checar código prefira usar Try -> Except
"""


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos os números precisam ser positivos'
    return a + b


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente'
    ], 'A comida precisa ser fast food'
    return f'Estou comendo {comida}!!!!'


pri = input('Informe o primeiro número: ')
seg = input('Informe o segundo número: ')
print(f'Teste de assertion número 1 => {soma_numeros_positivos(pri, seg)}')
comida = input('Informe seu pedido: ')
print(f'Teste de assertion número 2 => {comer_fast_food(comida)}')
