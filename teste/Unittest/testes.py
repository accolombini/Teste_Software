"""
Importante  -> quando executar o main o unittest irá percorrer o código e testarar tudo que encontrar com o nome test_
            -> outro ponto importante é que o Unitteste considera cada função um teste, logo se sua função realiza mais de um teste, falhando em um deles, os demais não serão realizados.

Para executar o teste, no terminal digite <=> python <nome_do_teste.py>

Exemplo de execução:
FFFF
======================================================================
FAIL: test_comer_gostosa (__main__.AtividadsTestes.test_comer_gostosa)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/accol/Library/CloudStorage/OneDrive-Pessoal/TESTES/T_Software_Python/teste/Unittest/testes.py", line 33, in test_comer_gostosa
    self.assertEqual(
AssertionError: None != 'Estou comendo pizza porque a gente só vive uma vez.'

======================================================================
FAIL: test_comer_saudavel (__main__.AtividadsTestes.test_comer_saudavel)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/accol/Library/CloudStorage/OneDrive-Pessoal/TESTES/T_Software_Python/teste/Unittest/testes.py", line 27, in test_comer_saudavel
    self.assertEqual(
AssertionError: None != 'Estou comendo quiabo porque quero manter a forma.'

======================================================================
FAIL: test_dormir_muito (__main__.AtividadsTestes.test_dormir_muito)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/accol/Library/CloudStorage/OneDrive-Pessoal/TESTES/T_Software_Python/teste/Unittest/testes.py", line 45, in test_dormir_muito
    self.assertEqual(
AssertionError: None != 'Ptz! Dormi muito! Estou atrasado para o trabalho!'

======================================================================
FAIL: test_dormir_pouco (__main__.AtividadsTestes.test_dormir_pouco)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/accol/Library/CloudStorage/OneDrive-Pessoal/TESTES/T_Software_Python/teste/Unittest/testes.py", line 39, in test_dormir_pouco
    self.assertEqual(
AssertionError: None != 'Continuo cansado após dormir por 4 horas. :('

----------------------------------------------------------------------
Ran 4 tests in 0.002s

FAILED (failures=4)

"""

import unittest

from atividades import comer, dormir, eh_engracada


class AtividadsTestes(unittest.TestCase):
    # def test_comer(self):  # Primeiro teste do TDD - Observe a aplicação da convenção no nome test_
    #     self.assertEqual(
    #         comer('quiabo', True),
    #         'Estou comendo quiabo porque quero manter a forma.'
    #     )
    #     self.assertEqual(
    #         comer(comida='pizza', eh_saudavel=False),
    #         'Estou comendo pizza porque a gente só vive uma vez.'
    #     )

    # Refatorando criando uma função para cada teste usando assim das melhores práticas

    # Primeiro teste do TDD - Observe a aplicação da convenção no nome test_
    def test_comer_saudavel(self):
        """Testando o retorno com comida saudável"""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comer_gostosa(self):
        """Testando o retorno com comida gostosa."""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez.'
        )

    def test_dormir_pouco(self):
        """Testando o retorno dormindo pouco."""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas. :('
        )

    def test_dormir_muito(self):
        """Testando o retorno dormindo muito."""
        self.assertEqual(
            dormir(10),
            'Ptz! Dormi muito! Estou atrasado para o trabalho!'
        )

    # def test_eh_engracada(self):  # Mais um passo do TDD
    #     """Testando o retorno para avaliar se uma pessoa é engraçada"""
    #     self.assertEqual(eh_engracada('Sérgio Malandro'), False)
    #     # self.asserFalse(eh_engracada('Sérgio Malandro'))

    def test_eh_engracada(self):
        # self.assertEqual(eh_engracada('Sérgio Malandro'), False)
        self.assertFalse(eh_engracada('Sérgio Malandro'))
        self.assertTrue(eh_engracada('Jim Carrey'),
                        'Jim Carrey deveria ser engraçado')


if __name__ == '__main__':
    unittest.main()
