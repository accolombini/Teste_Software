# Vamos nesta prática simular uma construção com a metodologia TDD
def duplicar(valores):
    """Dupica valores em uma lista
    >>> duplicar([1, 2, 3, 4, 5])
    [2, 4, 6, 8, 10]
    >>> duplicar([])
    []
    >>> duplicar(['a', 'b', 'c', 'd'])
    ['aa', 'bb', 'cc', 'dd']
    >>> duplicar([True, None])
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    pass  # Isso é TDD, criamos priemiro o teste e não inciamos a codificação
