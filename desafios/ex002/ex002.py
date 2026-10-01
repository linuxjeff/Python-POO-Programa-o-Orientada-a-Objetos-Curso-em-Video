# Declaração de classe
class Gafanhoto:
    """
    Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade.

    Para criar um gafanhoto, use
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome="Vazio", idade=0):
        # Atributo de intância
        self.nome = nome
        self.idade = idade

    # Metodos de instância

    def aniversario(self):
        self.idade += 1

    def __str__(self) -> str: # Dunder Merthod
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'

# Declaração de objeto
g1 = Gafanhoto("Maria", 17)
g1.aniversario()
print(g1.__getstate__())
