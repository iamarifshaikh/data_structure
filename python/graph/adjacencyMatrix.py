class GraphMatrix:
    def __init__(self,vertices):
        self.vertices = vertices
        
        # Initialize N x N matrix with all values set to 0
        self.matrix = [[0 for _ in range (vertices)]for _ in range (vertices)]

    def add_edge(self,node1,node2,directed=False):
        self.matrix[node1][node2] = 1
        if not directed:
            self.matrix[node2][node1] = 1  # For undirected graphs

    def display(self):
        print("Adjacency Matrix:")
        for row in self.matrix:
            print(row)
            
    