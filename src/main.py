from process_file import processFile
from process_file import buildNode
from graph import Graph

graph = Graph()
file = open("DADOS.txt")
buildNode(file, graph)
file.seek(0)
processFile(file, graph)
carga_horaria = float(input("Enter a weekly workload: "))
results_dict = graph.gulosoMaxValue(carga_horaria)

if(results_dict["Nodes"] == ""):
    print("Insufficient workload.")
else:
    print("The best path found was: ")
    print(results_dict["Nodes"])
    print("The profit on this week was: R$", results_dict["Gain"])
    graph.printGraph(graph.return_VisitedNodeList(results_dict["Nodes"]))
file.close()