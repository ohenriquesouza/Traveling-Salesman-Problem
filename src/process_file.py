from edge import Edge
from node import Node
from graph import Graph

def processFile(file, graph):
    for line in file:
        processLine(line, graph)


def processLine(line: str, graph):
    split = line.split(' ')
    getNumberOfNodes(split, graph)
    buildEdge(split, graph)

def getNumberOfNodes(split, graph):
    if (split[0] == "Vertices"):
        nmNodes = split[2].replace('\n', '')
        graph.setNmNodes(int(nmNodes))

def getFloatValueFromTitle(line, title):
        value_index = line.index(title) + 1
        value = line[value_index]
        try :
            value = value.replace('\n', '')
            return float(value)
        except:
            return float(value)


def buildEdge(split, graph):
    if (split[0][0] == '('):
        nodes = split[0][1:-1].split(',')
        for edge_info in split:
            if (edge_info == "distance"):
                distance = getFloatValueFromTitle(split, edge_info)

            if (edge_info == "gas_cost"):
                gas_cost = getFloatValueFromTitle(split, edge_info)



        begin = verifyNode(nodes[0], graph)
        end = verifyNode(nodes[1], graph)

        edge = Edge(
            gas_cost,
            distance,
            begin,
            end
        )
        build_NodeEdgeList(graph, edge)
        graph.addEdge(edge)

def verifyNode(node_id, graph):
    for i in graph.nodes:
        if (i.id == node_id):
            return i

def buildNode(file, graph):
    for line in file:
        split = line.split(' ')
    
        if (split[0][0] == '['):
            node_id = split[0][1:-1]
            for node_info in split:
                if(node_info == "bounty"):
                    bounty = getFloatValueFromTitle(split, node_info)

                if(node_info == "time_spent"):
                    time_spent = getFloatValueFromTitle(split, node_info)
            node = Node(
                node_id,
                bounty,
                time_spent
            )

            graph.addNode(node)

def build_NodeEdgeList(graph, edge):
    for i in graph.nodes:
        if (i == edge.begin):
            i.edges.append(edge)