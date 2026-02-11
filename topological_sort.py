from collections import deque
def find_topological_ordering(graph):
    n = len(graph)
    queue = deque()
    count_degree = [0] * (n+1)
    topo_order = [0] * (n+1)
    for i in range(n):
        count_degree[i] = count_degree[i] + 1
    
    for i in range(len(count_degree)):
        if count_degree[i] == 0:
            queue.append(count_degree[i])
    
    index = 0
    while queue:
        node = queue.popleft()
        topo_order[index+1] = node
        for dependent_node in graph[node]:
            count_degree[dependent_node] -= 1
            if count_degree[dependent_node] == 0:
                queue.append(dependent_node)
    if index!=n:
        return None
    return topo_order
        
            
        
        
        