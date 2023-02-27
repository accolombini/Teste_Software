"""
Vamos iniciar uma sequência de laboratórios abordando testes de software em Python

    ||> neste laboratório temos como objetivo compreender o uso e a importância dos Assertions

    ||> Vamos melhorar um pouco usando assert para levantar nossas próprias excessões. Farei outra função para
    manter o registro do processo de desenvolvimento.

    ||> Mas atenção a flag -O na execução do programa -> desabilita o uso das 'assertions': python -O nome_prog.py

        |||> Asserts são afirmações, onde o programador diz o que espera como resultado -> muito relevante quando
        outros progrmadores estão envolvidos no processo de desenvolvimento. Uma excessão é levantada e poderá ser
        trabalhada no processo de desenvolvimento.
"""


def soma(x, y):
    return x + y


def soma_assert(x, y):
    assert isinstance(x, (int, float)), f"x -> precisa ser um inteiro ou um float! Você entrou com -> {type(x)}"
    assert isinstance(y, (int, float)), f"y -> precisa ser um inteiro ou um float! Você entrou com -> {type(y)}"
    return x + y


if __name__ == "__main__":
    print(soma(10, "20"))
