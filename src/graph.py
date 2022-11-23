from itertools import permutations

from edge import Edge
from node import Node

import networkx as nx
from matplotlib import pyplot as plt

class Graph():
    
    def __init__(self):#construtor da classe Grafo
        self.edges: list[Edge] = [] #lista de arestas do grafo
        self.nmNodes : int = None #numero de vertices do grafo
        self.G = nx.DiGraph() #formação do grafo direcionado pela lib NetworkX
        self.nodes: list[Node] = [] #lista de vertices do grafo
        self.visitedEdges: list[Edge] = [] #lista de arestas já visitadas no grafo
        self.visitedNodes: list[Node] = [] #lista de vertices já visitados no grafo
        self.workload: int = 0 #carga horária
        self.gain: int = 0 #ganho total

    def addEdge(self, edge : Edge): #adiciona uma aresta no grafo
        self.edges.append(edge)
        self.G.add_edge(edge.begin.id, edge.end.id, length = edge.gas_cost, weight = edge.distance)

    def addNode(self, node : Node): #adiciona um vertice no grafo
        replica = False
        for i in self.nodes:
            if (node.id == i.id):
                replica = True
                break

        if (not replica):
            self.nodes.append(node)
                
    def printGraph(self, nodes): #printa e plota o grafo, utilizando as libs: networkX e matplot
        color_map = []
        pos = { #posições dos nós no plano cartesiano
            '0':([0.0, 0.0]),
            '1':([-0.2, 4.0]),
            '2':([5.5, 8.0]),
            '3':([8.0, 3.0]),
            '4':([10.0, -4.0]),
            '5':([1.0, -4.0]),
            '6':([0.3, -7.0]),
            '7':([-4.0, -3.8]),
            '8':([-4.5, 2.5]),
            '9':([-2.0, 6.0])            
        }
        
        for i in self.nodes:#loop que colorirá o grafo, verde os vértices já visitados e azul os não visitados
            if (self.existNode(i, nodes)):
                color_map.append('green')
            else:
                color_map.append('blue')
        
        nx.draw_networkx_edges(self.G, pos, edge_color= '#000000')
        nx.draw_networkx_nodes(self.G, pos, node_color=color_map)
        nx.draw_networkx_labels(self.G, pos)
        plt.show()

    def setNmNodes(self, nmNodes : int): #define o número de vértices do grafo
        self.nmNodes = nmNodes

    def verifyNode(self, node_id): #recebe um id de um vértice e verifica se este existe no grafo
        for i in self.nodes:
            if (i.id == node_id):
                return i

    def existNode(self, node, visitedNodes): #recebe um id de um vértice e verifica se este existe já foi visitado no grafo
        for i in visitedNodes:
            if (i == node):
                return True

        return False

    def return_VisitedNodeList(self, str): #retorna uma lista de vértices visitados no grafo
        split = str.split(' ')
        list = []
        for i in split:
            if (i.isalnum() and i != "home"):
                list.append(self.verifyNode(i))
        return list

    def verifyEdge(self, edge): #recebe uma aresta e verifica se esta ja foi percorrida no grafo
        for i in self.visitedEdges:
            if (i == edge):
                return True
        return False

    def find_BestStep(self, node): #função de caminhamento guloso
        max_bounty = 0
        canContinue = False

        for i in node.edges: #recebe um vértice 'node' e faz-se a seguinte verificação: o ganho do vértice da outra ponta da aresta possui um ganho maior que o já armazenado em 'max_bounty'? Com a carga-horária atual, é possível caminhar para este vértice em observação e voltar para divinópolis? A aresta a ser caminhada ja foi utilizada?
    
            if (i.end.bounty > max_bounty and i.end.time_spent < (self.workload - self.timeToReturn(i.end) - i.distance) and (not self.verifyEdge(i))):
                max_bounty = i.end.bounty
                best_node = i.end
                edge_passed = i 
                canContinue = True

        if(canContinue): #se foi possível dar um passo, adiciona o vértice na lista de visitados e atualiza o ganho e a carga-horária do grafo
            self.visitedNodes.append(best_node)
            node = best_node
            if (edge_passed.begin == self.nodes[0]):
                self.addEdge_NodeEdgeList(node)
            self.workload = self.workload - (best_node.time_spent + edge_passed.distance)
            self.gain = self.gain + (best_node.bounty - edge_passed.gas_cost)
        
        else: #se não foi possível dar o passo, volta para Divinópolis e atualiza o ganho e a carga-horária
            self.visitedNodes.append(self.nodes[0])
            self.workload = self.workload - self.timeToReturn(node)
            self.gain = self.gain - self.costToReturn(node)

        
        return node

    def gulosoMaxValue(self, workload): #recebe a carga horária semanal e roda o algoritmo guloso olhando todas as possibildades de caminho, fazendo um intermédio entre programação-dinâmica e guloso
        results_dict = {} #dicionário que armazenará o resultado final do algoritmo
        results_dict["Nodes"] = ""
        results_dict["Gain"] = self.gain
        
        for i in range (len(self.nodes[0].edges)): #enquando houver arestas saindo de divinópolis, rodará a função find_BestStep()
            self.cleanVariables(workload)
            no = self.nodes[0]
            self.visitedNodes.append(no)
            if (self.can_ChooseEdge(no)): #observa se há carga-horária suficiente para andar no grafo, pois há casos que há algumas arestas que não são possíveis de percorrer
                while (no != self.find_BestStep(no)):
                    no = self.visitedNodes[-1]
            else:
                break   

            if (self.gain > results_dict["Gain"]):
                results_dict["Nodes"] = self.returnVisitedNodes()
                results_dict["Gain"] = self.gain

        return results_dict

    def timeToReturn(self, node): #recebe um vértice e retorna o tempo necessário para voltar desse vertice para divinopolis
        for i in node.edges:
            if (i.end == self.nodes[0]):
                return i.distance

    def costToReturn(self, node): #recebe um vértice e retorna o custo com gasolina necessário para voltar desse vertice para divinopolis
        for i in node.edges:
            if (i.end == self.nodes[0]):
                return i.gas_cost

    def returnVisitedNodes(self): #retorna uma string apontando os vértices que foram caminhados
        str = ""
        for i in self.visitedNodes:
            str = str + i.id + " -> "

        str = str + "home"
        return str

    def printVisitedEdges(self): #printa as arestas visitadas
        for i in self.visitedEdges:
            print(i.begin.id," -> ", i.end.id)

    def addEdge_NodeEdgeList(self, node): #adiciona uma aresta na lista de arestas visitadas de um vértice específico
        for i in self.edges:
            if (node.id == i.end.id and i.begin == self.nodes[0]):
                self.visitedEdges.append(i)

    def cleanVariables(self, workload): #limpa todas as variáveis utilizadas no loop guloso-dinâmico
        self.workload = workload
        self.visitedNodes.clear()
        self.gain = 0

    def can_ChooseEdge(self, node): #retorna se é possível percorrer por alguma aresta no grafo
        for i in node.edges:
            if (i.end.time_spent < (self.workload - self.timeToReturn(i.end) - i.distance) and (not self.verifyEdge(i))):
                return True

        return False
