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

    def bfs(self,graph,start):
        visited = set() # 1. Queue begines with the start node.
        queue = deque([start]) # 2. Mark start as visited
        
        while queue: # 3. Process nodes until queue is empty.
            node = queue.popleft() # 4. Dequeue the front node (FIFO).
            
            if node not in visited:
                visited.add(node)     
                print(node) # 5. Mark node as visited
                               
            for neighbor in graph[node]: # 6. Enqueue all neighbors of node
                if neighbor not in visited: # 7. Mark node as visited
                    queue.append(neighbor) # 8. Add neighbor to the queue
                    visited.add(neighbor) # 9. Mark node as visited
    
    def dfs(self,graph,start):
        visited = set() # 1. Start by pushing the starting node onto the stack.
        stack = [start] # 2. Track visited node
        
        while stack: # 3. Process until the stack is empty
            node = stack.pop() # 4. Pop the top/first node
            if node not in visited: # 5. Only process unvisited nodes.
                visited.add(node) # 6. Mark current node as visited.
                print(node) # 7. Print the current node
            
            for neighbor in graph[node]: # 8. Push all neighbors of the current node onto the stack.
                if neighbor not in visited: # 9. if neighbor is not visited then process it.
                    stack.append(neighbor)  # 10. Add neighbor to the stack.
                    visited.add(neighbor) # 11. Mark neighbor as visited.