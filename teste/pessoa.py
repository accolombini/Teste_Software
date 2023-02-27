"""
Este módulo é parte integrante do laboratório teste de classes que continua aplicando Unittest agora em uma classe.
"""
import requests


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__dados_obtidos = False

    @property
    def nome(self):
        return self.__nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @property
    def dados_obtidos(self):
        return self.__dados_obtidos

    @dados_obtidos.setter
    def dados_obtidos(self, value):
        self.__dados_obtidos = value

    def obter_todos_os_dados(self):
        resposta = requests.get('https://pypi.org/project/requests/')  # Está uma conexão fake - ela nunca irá ocprrer.

        if resposta.ok:
            self.dados_obtidos = True
            return 'CONECTADO'
        else:
            self.dados_obtidos = False
            return 'ERRO 404'
