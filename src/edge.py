class Edge():

    def __init__(self, gas_cost, distance, begin, end):
        self.gas_cost = gas_cost
        self.distance = distance
        self.begin = begin
        self.end = end
        self.passed = False

    def printEdge(self):
        print(self.distance, self.gas_cost)