edge_list = [["Jeff","Fred"], ["Fred","Sara"],["Johanna", "Guilia"]]
vertex_list =  {x for l in edge_list for x in l}

from collections import deque 

def to_adjacency_list(vertex_list, edge_list, is_undirected):
  output = {}
  # Seed the adjacency list with all the vertices
  for v in vertex_list:
    output[v] = []
    
  # Build out the adjacency lists
  for node1, node2 in edge_list:
    output[node1].append(node2)
    # If the graph is undirected, you should also
    # make node2 point to node1
    if is_undirected:
      output[node2].append(node1)
  return output


adj_list = to_adjacency_list(vertex_list, edge_list, is_undirected=True)
print(adj_list)

def solution(adj_list):

    visited = set(["Fred"])
    queue = deque(["Fred"])
    while queue:
        curr_person = queue.popleft()
        for person in adj_list[curr_person]:
            
            visited.add(person)
    print('visited', visited)
    return len(visited) == len(adj_list)


print(solution(adj_list))
