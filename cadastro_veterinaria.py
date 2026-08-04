class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir(self):
        pass


class Cachorro(Animal):
    def exibir(self):
        return f"Cachorro: {self.nome}, {self.idade} anos"


class Gato(Animal):
    def exibir(self):
        return f"Gato: {self.nome}, {self.idade} anos"


cadastro = [
    Cachorro("Rex", 5),
    Gato("Mimi", 3)
]

print("Animais cadastrados:")
for animal in cadastro:
    print(animal.exibir())
