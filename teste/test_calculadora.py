"""
Trabalhando com testes em Python - Laboratórios 247-255

    ||> IMPORTANTE: - criou um método/classe/função <=> crie os TESTES
                    - não encare erros como problemas e sim como alertas
                    - muitas vezes o erro relfete a tentativa de fazer algo não previsto pelo métod/classe etc.

    Para estudos, consulte:
        https://docs.python.org/pt-br/3/library/unittest.html

        |||> Nos próximos laboratórios vamos trabalhar com UNITTEST

        |||> Para trabalhar com unittest é preciso importar o módulo unittest -> padrão do Python.
        |||> Crie uma classe para teste, essa classe deve herdar de unittest.TestCase
        |||> ATENÇÃO:   - dos os testes criados na classe de teste deverão iniciar com a palavra Test, caso se esqueça
        disso, os testes não serão executados.
                        - a classe criada é uma classe normal, poderá ser utilizada para trabalha sem problemas,
                        os testes acontecem mdediante a definição dos testes nesta classe, tendo os métodos iniciados
                        com a palavra test_.
        |||> Para executar os testes, basta utilizar o método unittest.main()


        ||> ATENÇÃO:   - para automatizar seus testes e executá-los todos de uma vez precisa se LEMBRAR de que
            todos os arquivos de testes devem iniciar com a palavra test -> essa é a referência de trabalho
            para o unittest.
                            - a automação é obtida através do comando: python -m unittest -v
"""

import unittest

from src.calculadora import soma


class TesCalculadora(unittest.TestCase):  # Nesta classe todos os testes deverão iniciar com a palavra 'test'

    def test_soma_5_e_5_deve_retornar_10(self):  # Tests que iniciam com a palavra 'test' não serão executados
        # Os nomes dos testes devem refletir com certa clareza o que está sendo feito e o que se espera
        self.assertEqual(soma(5, 5), 10)

    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5, 5), 0)

    def test_soma_varias_entradas(self):  # A forma recomendada é trabalhar com subtestes usando um gerenciador de
        # contexto -> with
        x_y_saidas = (  # Estamos criando uma tupla com várias possibilidades de testes
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3),
            (-5, 5, 0),
            (100, 100, 200),
        )
        for x_y_saida in x_y_saidas:  # Criando os subtestes
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida  # Captura os valores de x, y e saída
                self.assertEqual(soma(x, y), saida)

    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(TypeError):  # Teste antes com AssertionError
            soma('11', 0)

    def test_soma_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(TypeError):  # Teste antes com AssertionError
            soma(0, '11')


if __name__ == '__main__':
    unittest.main(verbosity=2)
