from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self):
        print("Constructor")
        self.graph = defaultdict(list)
        self.visited = []
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    # En anchura
    def BFS(self, s):
        
        parents = {}
        visited = {gi: False for gi in self.graph.keys()}
        queue = []
        queue.append(s)
        visited[s] = True
        
        while queue:
            s = queue.pop(0)
            print(s, end = " ")
            
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    parents[i] = s
                    
        return parents
                    
    
    def DFS(self, s):
        parents = {}
        visited = {gi: False for gi in self.graph.keys()}
        queue = []
        queue.append(s)
        visited[s] = True
        
        while queue:
            s = queue.pop()
            print(s, end = " ")
            
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    parents[i] = s
        
        return parents
        
                
        
                    
g = Graph()
g.addEdge('A', 'B')
g.addEdge('A', 'D')
g.addEdge('A', 'S')
g.addEdge('B', 'A')
g.addEdge('B', 'C')
g.addEdge('B', 'E')
g.addEdge('C', 'B')
g.addEdge('D', 'A')
g.addEdge('D', 'E')
g.addEdge('D', 'S')
g.addEdge('E', 'B')
g.addEdge('E', 'D')
g.addEdge('E', 'F')
g.addEdge('F', 'E')
g.addEdge('F', 'G')
g.addEdge('G', 'A')
g.addEdge('S', 'A')
g.addEdge('S', 'D')
# g.addEdge('A', 'B')
# g.addEdge('A', 'C')
# g.addEdge('B', 'A')
# g.addEdge('B', 'D')
# g.addEdge('B', 'E')
# g.addEdge('C', 'A')
# g.addEdge('C', 'F')
# g.addEdge('D', 'B')
# g.addEdge('E', 'B')
# g.addEdge('E', 'F')
# g.addEdge('F', 'C')
# g.addEdge('F', 'E')

print("\nBFS")
parentsBFS = g.BFS('S')
print("\nDFS")
parentsDFS = g.DFS('S')

def pathFromOrigin(origin, n, p):
    
    if origin == n:
        return []
    
    path = [n]
    i = n
    
    while True:
        i = p[i]
        path.insert(0, i)
        
        if i == origin:
            return path
      
print("\n")  
print(f"PATH BFS = {pathFromOrigin('S', 'G', parentsBFS)}")
print(f"PATH DFS = {pathFromOrigin('S', 'G', parentsDFS)}")