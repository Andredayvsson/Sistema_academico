from pessoa import Pessoa

class Funcionario_Administrativo:
    def _init_ (self, nome, idade, cargo):
        self.cargo = cargo
        super()._init_(nome,idade)

    def info(self):
        print ("As informações do(a) funcionário(a) são : ")
        print (f'nome: {self.nome}, idade: {self.idade}, cargo: {self.cargo}'