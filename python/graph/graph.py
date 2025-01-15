from collections import deque
from math import inf

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

    def bfs(self,start):
        visited = set() # to keep track of visited nodes and make sure we don't visit them again
        queue = deque([start]) # queue to keep track of nodes to visit queue.
        bfs_edge = [] # to keep track of the order of nodes visited

        # loop through the queue until it is empty
        while queue:
            vertex = (queue.popleft())  # remove the first element in the queue and assign it to vertex
            print(vertex,end="")
            if vertex not in visited: # if vertex is not visited then we need to add it to the visited set
                bfs_edge.append(vertex) # add visited node to the bfs_edge list
                for neighbor in visited[vertex]: # loop through the neighbors of the vertex
                    if neighbor not in visited: # if neighbor is not visited then we need to add it to the visited set
                        visited.add(neighbor) # add neighbor to the visited set
                        queue.append(neighbor) # add neighbor to the queue
        return bfs_edge

    def dfs(self,start,visited=None):
        pass