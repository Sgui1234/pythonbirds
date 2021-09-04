class Pessoa():
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=0):
        self.filhos = list(filhos)
        self.idade = idade
        self.nome = nome
    def cumprimentar(self,nome=None):
        self.nome = nome
        return f'Eae {nome}'
if __name__ == '__main__':
    name = input("Digite Seu Nome: ")
    age = int(input("Digite Quantos Anos Você Vai Fazer: "))
    p = Pessoa(name,age)
    fi = Pessoa(nome='Seus Filhos')
    pe = Pessoa(fi, nome=name)
    print(p.cumprimentar(name))
    print(f'{p.nome} Vai Fazer {p.idade} Anos')
    print(Pessoa.olhos, pe.olhos)
    for i in pe.filhos:
        print(i.nome)