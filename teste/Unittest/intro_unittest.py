"""
A sequencia de trabalhos deste diretório é:
    - intro_unittest.py -> traz os fundamentos e conceitos básicos do Unittest.
    - atividades.py -> módulo onde as atividades a serem testadas aplicando o conceito TDD serão construídas.
    - testes.py -> onde são criados os testes a partir da classe de testes que por padrão de melhorese práticas deve ter o mesmo nome do módulo a ser testado. Note que o arquivo de teste é separado da aplicação, ele faz parte do processo de desenvolvimento mas é separado, o que o torna independente de nossa aplicação.
Introdução ao módulo Unittest
    Unittest --> Testes Unitários
    Mas, o que são testes Unitários => é a forma de se testar unidades individuias de código fonte.
    Unidades individuais podem ser => funções, métodos, classes,módulos, etc.
    
    Seu objeto é mostrar que cada unidade atende às suas especificações.
    
    OBS.: quando se fala de testes unitários, não se fala especificamente de Python, mas sim do processo e da qualidade do software.
    
    - Para criar nossos testes, criamos classes que herdam de unittest.TestCase e a partir de então ganhamos todos os 'assertions' presentes no módulo. Estes assertons permite nos testar a unidade de software desejada com extremo rigor.
    
    TestCase -> casos de testes que serão aplicados na sua unidade a ser testada.
    É dentro da classe TestCase que herda de unittest que possui o memso nome da unidade a ser testada é que serão construídos os testes. Para gerar estes testes, fazemos usos de todas as Assertions presentes em TestCase. (recomenda-se com tempo ir testando e se familizarizando com todas). Uma versão completa de todas as Assertions pode ser encontrada em: https://docs.python.org/3/library/unittest.html 
    Uma boa dica aqui é iniciar pela tabela TestCase
    
    - Conhecendo as assertions (tabela TestCase)
    
    Método                            checa que
    assertEqual(a,b)                  a == b
    assertNotEqual(a,b)               a != b
    assertTrue(x)                     x é verdadeiro
    assertFalse(x)                    x é falso
    assertIs(a, b)                    a é b
    assertIsNot(a, b)                 a não é b
    assertIfNone(x)                   x é None
    assertIsNotNone                   x não é None
    assertIn(a, b)                    a está em b
    assertNotIn(a, b)                 a não está em b
    assertIsInstance(a, b)            a é instância de b
    assertNotIsInstance(a, b)         a não instância de b
    
    -> ATENÇÃO: por convenção, todos os testes em um test case, devem ter seu nome iniciado com test_
    _________________________________________________________________________________________
    - Para rodar os testes, utilizamos <=> unittest.main()
    - Para rodar os testes no terminal digitamos <=> python <nome_do_modulo.py>
    
    Nota: para executar os testes no modo verbose <=> python <nome_do_modulo.py> -v
    
    Dica: podemos acrescentar (e é recomendado) docstrings nos nossos testes. Estas docstrings serão resgatas quando se usar o método verbose.
    
"""

# Praticando -> utilizando a abordagem TDD
