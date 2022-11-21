from process_file import processFile
from process_file import buildNode
from graph import Graph

graph = Graph()
file = open("DADOS.txt")
buildNode(file, graph)
file.seek(0)
processFile(file, graph)
carga_horaria = float(input("Insira a carga horária desejada: "))
results_dict = graph.gulosoMaxValue(carga_horaria)
print("O melhor caminho encontrado foi: ")
print(results_dict["Nodes"])
print("Com um ganho de: R$", results_dict["Gain"])
graph.printGraph(graph.return_VisitedNodeList(results_dict["Nodes"]))
file.close()