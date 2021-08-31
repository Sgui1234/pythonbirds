class Pessoa():
    def __init__(self, nome=None, idade=0):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self,nome=None):
        self.nome = nome
        return f'Eae {nome}'
if __name__ == '__main__':
    name = input("Digite Seu Nome: ")
    age = int(input("Digite Quantos Anos Você Vai Fazer: "))
    p = Pessoa(name,age)
    print(p.cumprimentar(name))
    print(f'{p.nome} Vai Fazer {p.idade} Anos')