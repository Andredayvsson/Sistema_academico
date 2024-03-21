class Aluno(Pessoa):
    def _init_(self, nome, idade, matricula):
        super()._init_(nome, idade)
        self.matricula = matricula

    def info(self):
        return f"{super().info()}, Matrícula: {self.matricula}"
    
