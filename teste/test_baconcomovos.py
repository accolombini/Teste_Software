"""
    ||> ATENÇÃO:    - para automatizar seus testes e executá-los todos de uma vez precisa se LEMBRAR de que
        todos os arquivos de testes devem iniciar com a palavra test -> essa é a referência de trabalho
        para o unittest.
                    - a automação é obtida através do comando: python -m unittest -v
"""

import unittest
from src.baconcomovos import bacon_com_ovos


class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_levantar_assertion_error_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('0')  # Enviando algo não int para levantar a excessão: AssertionError: AssertionError
            # not raised

    def test_bacon_com_ovos_deve_retornar_bancom_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f"A entrada {entrada} não retornou a saída esperada {saida}"
                )

    def test_bacon_com_ovos_deve_retornar_passar_fome_se_entrada_nao_for_multiplo_de_3_e_5(self):
        entradas = (1, 4, 7, 8)
        saida = 'Passar fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f"A entrada {entrada} não retornou a saída esperada {saida}"
                )

    def test_bacon_com_ovos_deve_retornar_bacon_se_entrada_for_multiplo_de_3(self):
        entradas = (3, 6, 9, 12, 18, 21, 24)
        saida = 'Bacon'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f"A entrada {entrada} não retornou a saída esperada {saida}"
                )

    def test_bacon_com_ovos_deve_retornar_ovos_se_entrada_nao_for_multiplo_de_5(self):
        entradas = (10, 20, 40, 50)
        saida = 'Ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f"A entrada {entrada} não retornou a saída esperada {saida}"
                )



'''
============================= test session starts =============================
collecting ... collected 1 item

test_baconcomovos.py::TestBaconComOvos::test_bacon_com_ovos_deve_levantar_assertion_se_nao_receber_int 
PASSED [100%]

============================== 1 passed in 0.02s ==============================
'''

if __name__ == '__main__':
    unittest.main(verbosity=2)
