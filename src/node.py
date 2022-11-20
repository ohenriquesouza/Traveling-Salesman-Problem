from edge import Edge

class Node():

    def __init__(self, id, bounty, time_spent):
        self.id = id
        self.bounty = bounty
        self.time_spent = time_spent
        self.edges : list[Edge] = []

    def addEdge(self, edge, bounty, time_spent):
        self.edges.append(edge)
        self.bounty = bounty
        self.time_spent = time_spent

    def printNode(self):
        print(self.id, self.bounty, self.time_spent)