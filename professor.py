from pessoa import Pessoa

class Professor:
    def __init__(self, nome, idade, disciplina):
        self.disciplina = disciplina
        super().__init__(nome, idade)
    
    def info (self):
        print('As informações do(a) professor(a) são:')
        print(f'Nome: {self.nome}, Idade: {self.idade}, Disciplina: {self.disciplina}')
