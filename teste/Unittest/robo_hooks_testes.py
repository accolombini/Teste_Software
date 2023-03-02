"""
Preparando o ambiente de testes
"""
import os
import unittest

from robo_hooks import Robo


class RoboHooksTestes(unittest.TestCase):
    # Neste teste simples queremos avaliar se o método carrgar retorna ao robo uma carga de 100%. Neste primeiro passo não estamos usando antes e depois dos hooks
    # def test_carregar(self):
    #     megaman = Robo('Mega Man', bateria=50)
    #     megaman.carregar()
    #     self.assertEqual(megaman.bateria, 100)

    # # Neste teste simples queremos fazer o robo dizer seu nome e avaliar se ele descarrega a bateria.
    # def test_dizer_nome(self):
    #     megaman = Robo('Mega Man', bateria=50)
    #     self.assertEqual(megaman.dizer_nome(),
    #                      'BEEP BOOP BEEP BOOP. Eu sou MEGA MAN')
    #     self.assertEqual(megaman.bateria, 49, 'A bateria deveria estar em 49%')

    # def test_carregar(self):
    #     megaman = Robo('Mega Man', bateria=50)
    #     megaman.carregar()
    #     self.assertEqual(megaman.bateria, 100)

    # Vamos agora refatorar nosso código para fazer uso de antes e depois de hooks.
    # Vamos definr setUp() com aquilo que se repete em todos os módulos
    # ATENÇÃO: note que o acesso será via -> self

    def setUp(self):
        self.megaman = Robo('Mega Man', bateria=50)
        print('\nserUp() sendo executado ....')

    def test_carregar(self):
        # megaman = Robo('Mega Man', bateria=50)
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def test_dizer_nome(self):
        # megaman = Robo('Mega Man', bateria=50)  -> Repetido
        self.assertEqual(self.megaman.dizer_nome(),
                         'BEEP BOOP BEEP BOOP. Eu sou MEGA MAN')
        self.assertEqual(self.megaman.bateria, 49,
                         'A bateria deveria estar em 49%')

    def tearDown(self):
        # path = '/Users/accol/Library/CloudStorage/OneDrive-Pessoal/TESTES/T_Software_Python/teste/unittest'
        # dir = os.listdir(path)
        # for file in dir:
        #     if file == 'teste.txt':
        #         os.remove(path + '/' + file)
        #         print("Arquivo foi deletado")
        #     else:
        #         print("Arquivo não encotrado - tudo limpo")
        print('\nEmbora desnecessário neste caso, segue para percebermos sua execução!')


if __name__ == '__main__':
    unittest.main()
