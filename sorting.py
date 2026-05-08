# A DAG graph will be represented using a edge list, where each element of this list will include
# a tuple with 2 nodes are connected with an edge
# for example: [(4, 1), (1, 3)] means this graph has nodes 1, 3 and 4.
# Node 1 is connected to both nodes 4 and 3.

# This function implements topological sorting of a DAG
#       - should be able to detect if a loop is present.
#       - should return the ordered sorting of nodes

def topological_sort(nodes: int, edges: list) -> list:
    
    #Adj.list
    graph={i: [] for i in range(nodes)}
    #edges count store
    indegree = [0] * nodes
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
        
    #node with no edges
    queue = []
    for i in range(nodes):
        if indegree[i] == 0:
            queue.append(i)
    order = []
    #process nodes loop
    while queue:
        current = queue.pop(0)
        order.append(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    #cycle throu the rest of the nodes that weren't visited
    if len(order) != nodes:
        print("loop detected")
        return []

    return order
