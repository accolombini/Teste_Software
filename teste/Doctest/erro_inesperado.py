"""
Simulando um erro inesperado
Neste erro o problema decorre de estarmos dentro das aspas triplas que não reconhece aspas duplas em seu interior, observe.

    OBS.: dentro do doctest, o Python não reconhece string com aspas duplas. Precisa ser aspas simples.
"""


def fala_oi():
    """Falaoi
    >>> fala_oi()
    "oi"
    """
    return "oi"
