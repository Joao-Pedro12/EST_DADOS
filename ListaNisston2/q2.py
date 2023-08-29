class Livro:

    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
    
    def detalhes(self):
        print(f'Nome:{self.nome}')
        print(f'autor {self.autor}')

p1 = Livro("GAME OF THRONES", "GEORGE")
p1.detalhes()