from itertools import permutations

from edge import Edge
from node import Node

import networkx as nx
from matplotlib import pyplot as plt

class Graph():
    
    def __init__(self):
        self.edges: list[Edge] = []
        self.nmNodes : int = None
        self.G = nx.DiGraph()
        self.nodes: list[Node] = []
        self.visitedEdges: list[Edge] = []
        self.visitedNodes: list[Node] = []
        self.workload: int = 0
        self.gain: int = 0

    def addEdge(self, edge : Edge):
        self.edges.append(edge)
        self.G.add_edge(edge.begin.id, edge.end.id, length = edge.gas_cost, weight = edge.distance)

    def addNode(self, node : Node):
        replica = False
        for i in self.nodes:
            if (node.id == i.id):
                replica = True
                break

        if (not replica):
            self.nodes.append(node)
                
    def printGraph(self, nodes):
        color_map = []
        pos = {
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
        
        for i in self.nodes:
            if (self.existNode(i, nodes)):
                color_map.append('green')
            else:
                color_map.append('blue')
        
        nx.draw_networkx_edges(self.G, pos, edge_color= '#000000')
        nx.draw_networkx_nodes(self.G, pos, node_color=color_map)
        nx.draw_networkx_labels(self.G, pos)
        plt.show()

    def setNmNodes(self, nmNodes : int):
        self.nmNodes = nmNodes

    def adjMatrix(self):
        return nx.to_numpy_matrix(self.G)

    def verifyNode(self, node_id):
        for i in self.nodes:
            if (i.id == node_id):
                return i

    def existNode(self, node, visitedNodes):
        for i in visitedNodes:
            if (i == node):
                return True

        return False

    def return_VisitedNodeList(self, str):
        split = str.split(' ')
        list = []
        for i in split:
            if (i.isalnum() and i != "home"):
                list.append(self.verifyNode(i))
        return list

    def verifyEdge(self, edge):
        for i in self.visitedEdges:
            if (i == edge):
                return True
        return False

    def find_BestStep(self, node):
        max_bounty = 0
        canContinue = False

        for i in node.edges: 
 
            if (i.end.bounty > max_bounty and i.end.time_spent < (self.workload - self.timeToReturn(i.end) - i.distance) and (not self.verifyEdge(i))):
                max_bounty = i.end.bounty
                best_node = i.end
                edge_passed = i 
                canContinue = True

        if(canContinue):
            self.visitedNodes.append(best_node)
            node = best_node
            if (edge_passed.begin == self.nodes[0]):
                self.addEdge_NodeEdgeList(node)
            self.workload = self.workload - (best_node.time_spent + edge_passed.distance)
            self.gain = self.gain + (best_node.bounty - edge_passed.gas_cost)
        
        else:
            self.visitedNodes.append(self.nodes[0])
            self.workload = self.workload - self.timeToReturn(node)
            self.gain = self.gain - self.costToReturn(node)

        
        return node

    def gulosoMaxValue(self, workload):
        results_dict = {}
        results_dict["Nodes"] = ""
        results_dict["Gain"] = self.gain
        
        for i in range (len(self.nodes[0].edges)):
            self.cleanConstants(workload)
            no = self.nodes[0]
            self.visitedNodes.append(no)
            if (self.can_ChooseEdge(no)):
                while (no != self.find_BestStep(no)):
                    no = self.visitedNodes[-1]
            else:
                break   

            if (self.gain > results_dict["Gain"]):
                results_dict["Nodes"] = self.printVisitedNodes()
                results_dict["Gain"] = self.gain

        return results_dict

    def timeToReturn(self, node):
        for i in node.edges:
            if (i.end == self.nodes[0]):
                return i.distance

    def costToReturn(self, node):
        for i in node.edges:
            if (i.end == self.nodes[0]):
                return i.gas_cost

    def printVisitedNodes(self):
        str = ""
        for i in self.visitedNodes:
            str = str + i.id + " -> "

        str = str + "home"
        return str

    def printVisitedEdges(self):
        for i in self.visitedEdges:
            print(i.begin.id," -> ", i.end.id)

    def addEdge_NodeEdgeList(self, node):
        for i in self.edges:
            if (node.id == i.end.id and i.begin == self.nodes[0]):
                self.visitedEdges.append(i)

    def cleanConstants(self, workload):
        self.workload = workload
        self.visitedNodes.clear()
        self.gain = 0

    def can_ChooseEdge(self, node):
        for i in node.edges:
            if (i.end.time_spent < (self.workload - self.timeToReturn(i.end) - i.distance) and (not self.verifyEdge(i))):
                return True

        return False
