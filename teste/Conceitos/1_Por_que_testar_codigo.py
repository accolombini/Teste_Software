""" 
Por que devemos testar nosso código?
Especificamente estamos aqui falando de testes automatizados.
 
Imagine que sua aplicação seja uma aplicação web dividido da seguinte forma:

--------------------------------------------------------
|                 frontend e backend                    |
--------------------------------------------------------
|                 testes automatizados                  |
________________________________________________________

Além desses dois (back e front devemos criar o sistema de testes.
Estes testes são criados por desenvolvedores e este tema pode ser polêmico, porque
estes testes automáticos exigem um esforço extra para o desenvolvimento de testes automatizados e possam ser realizados. É por isso, que grandes empresas investem num profissional com o perfil de tester.

Então por que testamos?
    - Reduzir bugs (problemas) no código existente;
    - Testes garantem que novos recursos da sua aplicação não quebrem (alterem) recursos antigos;
    - Testes garantem que bugs (problemas) que foram corrigidos anteriormente continuem corrigidos;
    - testes garantem que a refatoração que costumamos a fazer não tragam novos bugs (problemas);
    
    TDD - Test Driven Development (Desenvolvimento guiado por Testes) --> nesta vertente, primeiro escrevemos o teste e depois vamos desenvolvendo o código. Podemos dizer que trabalhamos com estágios de desenvolvimento.
        - Você escreve seu teste primeiro;
        - Então você escreve o código mínimo suficiente para fazer o teste passar (ou seja, executar com sucesso seu código de testes);   
        - Então refatora o código para realizar a funcionalidade e testa novamente;
        - Uma vez que o teste passe, o recurso é considerado completo;
        
    Estes estágios de desnvolvimento do TDD são quase que um mantra, que os desenvolvedores seguem, conhecidos como:
        - Red;  --> inicial - erros vermelho
        - Green;  --> final códio passa por todos os testes
        - Refactor;  --> intermediário refatora-se o código na busca de soluções que atendam os testes propostos.
   
"""


class Gato:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} esta miando muito ...')


# Teste a moda antiga -> teste de mesa (teste manual)

felix = Gato('Felix')  # Instanciando um objeto
felix.miar()  # Executa o método miar
print(f'{felix.nome} --> é o nome do Gato!!!')  # Imprime o nome do gato
