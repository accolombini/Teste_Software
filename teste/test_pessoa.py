"""
Continuamos neste laboratório trabalhando com Unittest. Para este laboratório vamos simular uma
situação onde não temos o controle, isto é não sabemos qual a condição que vamos encontrar no Servidor, que poderá
estar up ou down.

    ||> Vamos estruturar uma classe da seguinte forma:

        class Pessoa:
            __init__(self):
                nome str
                sobrenome str
                dados_obtidos bool (inicia com False)

            API:
                obter_todos_os_dados -> method
                    Ok
                    404
                    dados_obtidos se torna True se dados foram obtidos com sucesso


            |||> NOTA:  - para a API será feita uma requisição para fora da classe -> será usado um REQUEST para este
            laboratório.
                        - Pode ser que precise instalar o módulo request: pip install requests

            |||> ATENÇÃO:   - para automatizar seus testes e executá-los todos de uma vez precisa se LEMBRAR de que
            todos os arquivos de testes devem iniciar com a palavra test -> essa é a referência de trabalho
            para o unittest.
                            - a automação é obtida através do comando: python -m unittest -v

        Exemplo de execução de todos os testes. Note que você executa estando dentro do diretório dos arquivos
        testes, isso nem sempre é requsito, deverá sempre conferir seu ambiente de tetes:
        (p3oo)d:p3oo>python -m unittest

        .............
        ----------------------------------------------------------------------
        Ran 13 tests in 0.002s

        ovos.TestBaconComOvos) ... ok
        test_bacon_com_ovos_deve_retornar_bancom_com_ovos_se_entrada_for_multiplo_de_3_e_5
        (test_baconcomovos.TestBaconComOvos) ... ok
        test_bacon_com_ovos_deve_retornar_ovos_se_entrada_nao_for_multiplo_de_5 (test_baconcomovos.TestBaconComOvos)
        ... oktest_bacon_com_ovos_deve_retornar_passar_fome_se_entrada_nao_for_multiplo_de_3_e_5
        (test_baconcomovos.TestBaconComOvos) ... oktest_soma_5_e_5_deve_retornar_10
        (test_calculadora_unittest.TesCalculadora) ... ok
        test_obter_todos_os_dados_falha_404 (test_pessoa.TestPessoa) ... oktest_obter_todos_os_dados_sucesso_ok
        (test_pessoa.TestPessoa) ... ok
        test_pessoa_attr_dados_obtidos_inicia_false (test_pessoa.TestPessoa) ... oktest_pessoa_attr_nome_e_str
        (test_pessoa.TestPessoa) ... ok
        test_pessoa_attr_nome_tem_o_valor_correto (test_pessoa.TestPessoa) ...
        oktest_pessoa_attr_sobrenome_tem_o_valor_correto (test_pessoa.TestPessoa) ... ok
        test_pessoa_attr_sobrnome_e_str (test_pessoa.TestPessoa) ... ok

        ----------------------------------------------------------------------
        Ran 13 tests in 0.004s

        OK
"""

import unittest
from unittest.mock import patch  # Este módulo nos prermite a criação de dados fakes para aprimorar ainda mais os testes
from src.pessoa import Pessoa


class TestPessoa(unittest.TestCase):
    def setUp(self):  # Método de unittest que permite que a classe seja instanciada internamente à classe de  TESTE.
        self.p1 = Pessoa('Luiz', 'Otávio')
        self.p2 = Pessoa('Arthur', 'Dutra')

    def test_pessoa_attr_nome_tem_o_valor_correto(self):  # A partir daqui inicia-se os testes propriamente dito.
        self.assertEqual(self.p1.nome, 'Luiz')
        self.assertEqual(self.p2.nome, 'Arthur')

    def test_pessoa_attr_sobrenome_tem_o_valor_correto(self):  # Este na sequência é o segundo teste.
        self.assertEqual(self.p1.sobrenome, 'Otávio')
        self.assertEqual(self.p2.sobrenome, 'Dutra')

    def test_pessoa_attr_dados_obtidos_inicia_false(self):  # Este na sequência é o terceiro teste.
        self.assertFalse(self.p1.dados_obtidos)
        self.assertFalse(self.p2.dados_obtidos)

    def test_pessoa_attr_nome_e_str(self):  # Este na sequência é o quarto teste (observe que na execução será o
        # segundo.
        self.assertIsInstance(self.p1.nome, str)
        self.assertIsInstance(self.p2.nome, str)

    def test_pessoa_attr_sobrnome_e_str(self):  # Este na sequência é o quinto teste
        self.assertIsInstance(self.p1.sobrenome, str)
        self.assertIsInstance(self.p2.sobrenome, str)

    '''
    Tudo certo até aqui - passos a escrever os testes para a API - Atenção não queremos que o teste falhe por
    problemas externos ao código, sendo assim usaremos de recursos fake para garantir o teste e portanto o código,
    no contexto real a aplicação falahará se o ambiente externo não responder, mas terá as excessões levantadas
    '''

    def test_obter_todos_os_dados_sucesso_ok(self):  # Atenção OK vem da aplicação (modo Request) -> daí seu destaque
        with patch('requests.get') as fake_request:  # Observe o uso do mock -> patch permitindo a criação de dados fake
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)  # Estamos garantindo que uma vez conectado -> dados_obtidos passe
            # a ser True

            self.assertEqual(self.p2.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p2.dados_obtidos)  # Estamos garantindo que uma vez conectado -> dados_obtidos passe
            # a ser True

    def test_obter_todos_os_dados_falha_404(self):  # Agora vamos testar a falha (modo Request)
        with patch('requests.get') as fake_request:  # Observe o uso do mock
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)  # Estamos garantindo que uma vez não conectado -> dados_obtidos
            # seja atribuído como False

            self.assertEqual(self.p2.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p2.dados_obtidos)  # Estamos garantindo que uma vez não conectado -> dados_obtidos
            # seja atribuído como False


if __name__ == '__main__':
    unittest.main(verbosity=2)
