def bfs(graph, start, va, vb):
  queue = [start]
  path = []
  while queue != []:
    if va in path and vb in path: return True
    current = queue.pop()
    if current not in path: 
      path.append(current)
      for i in graph[current]:
        if i not in queue: queue.insert(0, i)
  return False

graph = {1: [2, 3],
         2: [1, 4, 5, 6],
         3: [1, 4],
         4: [2, 3, 5],
         5: [2, 4, 6],
         6: [2, 5]}
         
print bfs(graph, 1, 3, 5)