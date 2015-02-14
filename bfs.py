from collections import deque

"""
         A
    B         C
  D   E     F
G
"""
graph = {
  'A': set(['B', 'C']),
  'B': set(['D', 'E']),
  'C': set(['F']),
  'D': set(['G'])
}

# Note: 'graph' assumed to be without cycles
def bfs(graph_root, graph):
  nodes_queue = deque([graph_root])
  while nodes_queue:
    current_node = nodes_queue.popleft()
    print current_node
    nodes_queue.extend(graph.get(current_node, []))

