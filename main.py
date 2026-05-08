# TEAM DETAILS
# Ahmed Abd Al Moneim
# Details: 
#       ID: 9284
#       Group: 3
#       Section: 1
#
# Andrew Sameh
# Details:
#       ID: 9489
#       Group: 3
#       Section: 1
#
# Galal Mohamed
# Details:
#       ID: 9453
#       Group: 3
#       Section: 1

from sorting import topological_sort
from prim import prims

def main():
    # ADD TEST CASES HERE
    graph = {
        0: [(1, 2), (3, 6)],
        1: [(0, 2), (2, 3), (3, 8), (4, 5)],
        2: [(1, 3), (4, 7)],
        3: [(0, 6), (1, 8), (4, 9)],
        4: [(1, 5), (2, 7), (3, 9)]
    }

    edges, weight = prims(5, graph, 0)
    print(f"MST Edges: {edges}")
    print(f"Total MST Weight: {weight}")

if __name__ == "__main__":
    main()