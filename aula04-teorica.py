def exemplo01():
        #Classe com atributos (dados) e métodos (funções)
    class Cachorro:
        #self explicita determinada istância da classe que esta sendo estipulada
        #Método01 Construtor, precisa de __init__ para ser reconhecido como Método construtor
        def __init__(self, nome, idade): 
            self.nome = nome
            self.idade = idade

        #Método02
        def latir(self):
            print(f"{self.nome} está latindo")
            
        #Método02
        def idade_de_cachorro(self):
            print(f"{self.nome} tem {self.idade} anos de vida, e está latindo")
            

    nome_do_cao = input("digite o name: ")
    idade_do_cao = int(input("qual é a idade: "))

    #Criando um objeto da Classe Cachorro
    meu_cachorro = Cachorro(nome_do_cao, idade_do_cao) #Quando uma classe e posta em uma váriavel chamamos-a de Instância
    print(meu_cachorro.nome) #Acessa o atributo 'nome'
    meu_cachorro.latir() #Chamando o método latir
    meu_cachorro.idade_de_cachorro()


def exemplo1_test():
    class Gato:
    #self explicita determinada istância da classe que esta sendo estipulada
    #Método01 Construtor, precisa de __init__ para ser reconhecido como Método construtor
        def __init__(self, nome, idade): 
            self.nome = nome
            self.idade = idade

        #Método02
        def miar(self):
            print(f"{self.nome} está miando")
            
        #Método02
        def idade_de_gato(self):
            print(f"{self.nome} tem {self.idade} anos de vida, e está miando")
        

    nome_do_cao = input("digite o name: ")
    idade_do_cao = int(input("qual é a idade: "))

    #Criando um objeto da Classe gato
    meu_gato = Gato(nome_do_cao, idade_do_cao) #Quando uma classe e posta em uma váriavel chamamos-a de Instância
    print(meu_gato.nome) #Acessa o atributo 'nome'
    meu_gato.miar() #Chamando o método miar
    meu_gato.idade_de_gato()


def exemplo02():
    class Classielison:
        variavel_de_classe = 0
        def __init__(self):
            Classielison.variavel_de_classe += 1
    a = Classielison()
    b = Classielison()
    c = Classielison()
    print(Classielison.variavel_de_classe)

def exemplo03():
    class Classielison:
        def __init__(self, valor):
            self.variavel_de_instancia = valor
    a = Classielison(10)
    b = Classielison(20)
    c = Classielison(30)
    print(a.variavel_de_instancia)
    print(b.variavel_de_instancia)
    print(c.variavel_de_instancia)

# exemplo01()
# exemplo1_test()
# exemplo02()
# exemplo03()