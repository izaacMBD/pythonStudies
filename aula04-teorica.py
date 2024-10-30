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
digite = int(input("Digite 0 ou 1: "))


#Criando um objeto da Classe Cachorro
meu_cachorro = Cachorro(nome_do_cao, idade_do_cao) #Quando uma classe e posta em uma váriavel chamamos-a de Instância
numeros = [meu_cachorro.idade_de_cachorro(), meu_cachorro.latir()]

if digite != 0 and digite != 1:
    print("Vai se fuder")
else:
    print(numeros(digite))
