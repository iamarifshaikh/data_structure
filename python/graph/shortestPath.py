from collections import deque

def bfs_shortest_path(graph,start,end):
    visited = set()
    queue = deque([(start,0)])
    
    while queue:
        node,distance = queue.popleft()
        
        if node == end:
            return distance
        
        if node not in visited:
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor,distance + 1))

    return -1