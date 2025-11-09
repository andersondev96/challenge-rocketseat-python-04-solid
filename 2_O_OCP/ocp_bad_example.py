from abc import ABC, abstractmethod

'''
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle). 
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

'''

class Exame(ABC):
    @abstractmethod
    def verifica_condicoes(self):
        pass
    def aprovar_solicitacao_exame(self):
        pass


class ExameDeSangue(Exame):
    def verifica_condicoes(self):
        pass

    def aprovar_solicitacao_exame(self):
        print("Exame sanguíneo aprovado")

class ExameDeRaioX(Exame):
    def verifica_condicoes(self):
        pass

    def aprovar_solicitacao_exame(self):
        print("Raio-X aprovado")

class AprovadorDeExames:
    def aprovar(self, exame: Exame):
        exame.aprovar_solicitacao_exame()

# Exemplo de uso:
if __name__ == "__main__":
    aprovador = AprovadorDeExames()

    exame_sangue = ExameDeSangue()
    exame_raio_x = ExameDeRaioX()

    aprovador.aprovar(exame_sangue)
    aprovador.aprovar(exame_raio_x)