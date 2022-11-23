from edge import Edge
from node import Node
from graph import Graph

def processFile(file, graph): #separa o arquivo por linhas
    for line in file:
        processLine(line, graph)

def processLine(line: str, graph): #separa o arquivo removendo espaços entre strings
    split = line.split(' ')
    getNumberOfNodes(split, graph)
    buildEdge(split, graph)

def getNumberOfNodes(split, graph): #pesquisa no arquivo o número de vértices do grafo
    if (split[0] == "Vertices"):
        nmNodes = split[2].replace('\n', '')
        graph.setNmNodes(int(nmNodes))

def getFloatValueFromTitle(line, title): #retorna como float dado uma string do arquivo removendo possíveis '\n' no final da string
        value_index = line.index(title) + 1
        value = line[value_index]
        try :
            value = value.replace('\n', '')
            return float(value)
        except:
            return float(value)


def buildEdge(split, graph): #constrói uma aresta de acordo com os dados lidos no arquivo
    if (split[0][0] == '('):
        nodes = split[0][1:-1].split(',')
        for edge_info in split:
            if (edge_info == "distance"):
                distance = getFloatValueFromTitle(split, edge_info) #pega a distancia

            if (edge_info == "gas_cost"):
                gas_cost = getFloatValueFromTitle(split, edge_info) #pega o custo de gasolina



        begin = verifyNode(nodes[0], graph) #adiciona o vértice inicial da aresta
        end = verifyNode(nodes[1], graph) #adiciona o vértice final da aresta

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

def buildNode(file, graph): #constrói um vértice de acordo com os dados lidos no arquivo
    for line in file:
        split = line.split(' ')
    
        if (split[0][0] == '['):
            node_id = split[0][1:-1]
            for node_info in split:
                if(node_info == "bounty"):
                    bounty = getFloatValueFromTitle(split, node_info) #define a recompensa daquela cidade

                if(node_info == "time_spent"):
                    time_spent = getFloatValueFromTitle(split, node_info) #define o tempo gasto naquela cidade
            node = Node(
                node_id,
                bounty,
                time_spent
            )

            graph.addNode(node)

def build_NodeEdgeList(graph, edge): #adiciona uma aresta na lista de arestas de um vértice específico
    for i in graph.nodes:
        if (i == edge.begin):
            i.edges.append(edge)