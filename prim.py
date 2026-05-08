# Uses an adjacency list to represent nodes and their neighbors along with the weight of each edge
# for example: { 0: [(1, 2), (3, 6)] } -> has nodes 0, 1 and 3. Node 0 is connected to node 1 of weight 2 and with node 3 of weight 6

import heapq

def prims(nodes: int, adj: map, start_node: int):
    edges = []
    visited = [False] * nodes
    
    # Min-heap stores (weight, to_node, from_node)
    min_heap = [(0, start_node, -1)]
    total_weight = 0
    
    while min_heap:
        weight, u, prev_node = heapq.heappop(min_heap)
        
        # Make sure edge isn't visited before
        if visited[u]:
            continue
            
        # Mark it visited
        visited[u] = True
        # Add its weight to total
        total_weight += weight
        
        # Add it to MST edges       
        if prev_node != -1: edges.append((prev_node, u, weight))
            
        # Explore neighbors
        for v, w in adj[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v, u))
                
    print("MST Weight: ", total_weight)
    return edges