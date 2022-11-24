from edge import Edge

class Node():

    def __init__(self, id, bounty, time_spent):#construtor da classe do Vertice iniciando: a cidade que representa, seus pesos e a lista de arestas que o mesmo possui
        self.id = id
        self.bounty = bounty
        self.time_spent = time_spent
        self.edges : list[Edge] = []

    def printNode(self):
        print(self.id, self.bounty, self.time_spent)