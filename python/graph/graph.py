class Graph:
    def __init__(self):
        self.adjacency_list = {}
        
    def add_node(self,node):
        """Add a node to the graph"""
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []
        else:
            print(f"Node {node} already exists!")
    
    def add_edge(self,node1,node2, directed=False):
        """Add an edge to the graph"""
        if node1 in self.adjacency_list and node2 in self.adjacency_list:
            self.adjacency_list[node1].append(node2)
        if not directed:
            self.adjacency_list[node2].append(node1)
            
    def display(self):
        """Prints the graph."""
        for node,neighbors in self.adjacency_list.items():
            print(f"{node} -> {neighbors}")