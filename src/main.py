import linecache
from process_file import processFile
from process_file import buildNode
from graph import Graph

graph = Graph()
file = open("DADOS.txt")
buildNode(file, graph)
file.seek(0)
processFile(file, graph)
# A = [[0, 0.7, 2.4, 2, 3.2, 1, 1.2, 1.6, 0, 0],
#  [0.7, 0, 0, 1.8, 0, 0, 0, 0, 0, 0.6],
#  [2.4, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#  [2, 0, 0, 0, 1.5, 0, 0, 0, 0, 0],
#  [3.2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [1, 0, 0, 0, 0, 0, 0, 0, 0.7, 0],
#  [1.2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [1.6, 0, 0, 0, 0, 0, 1.1, 0, 0, 0],
#  [1.1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [1.1, 0, 0, 0, 0, 0, 0, 0.9, 0, 0]]
carga_horaria = float(input("Insira a carga horária desejada: "))
results_dict = graph.gulosoMaxValue(carga_horaria)
print("O melhor caminho encontrado foi: ")
print(results_dict["Nodes"])
print("Com um ganho de: R$", results_dict["Gain"])
# graph.printGraph()
file.close()