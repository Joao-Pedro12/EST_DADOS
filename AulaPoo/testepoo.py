class aluno:
    def __init__(self,nome,nota1,nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0.0

    def media_aluno(self):
        self.media = (self.nota1 + self.nota2) / 2
        return self.media

    def aprovado(self):
        if self.media >= 6:
            print("APROVADO")
        else:
            print("REPROVADO")

    def mostrar_dados(self):
        print(self.nota1)
        print(self.nota2)
        print(self.media_aluno)

p1 = aluno('jp', 7.00,7.00)
p1.media_aluno()
p1.aprovado()