"""
Unittest -> antes e após hooks

    Hooks -> são os teste em si. Ou seja, a execução dos testes. Assim, antes e após hooks, estamos dizendo que há algo a ser realizado antes e após a realização dos testes.
    
    - O que vem antes dos testes?
        setup() -> setup é executado antes de cada método de teste. É útil para criarmos instâncias de objetos e outros dados:
    - O que vem depois dos testes?
        tearDown() -> tear down é executado ao final de cada método de teste. é útil para excluir dados ou fechar conexões com banco de dados (quando for o caso).
"""

import unittest

class ModuloTest(unittest.TestCase):
    def setUp(self):
        # Aqui define-se as configurações do setUp()
        pass
    
    def test_primeiro(self):
        # setUp() vai rodar antes dos testes
        # tearDown() vai rodar após os testes
        pass

    def test_segundo(self):
        # setUp() vai rodar antes do teste
        # tearDown() vai rodar após os testes
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass
    
    
        