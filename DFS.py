def dfs(graph,start):
  path = []
  stack = [start]
  while stack != []:
    current = stack.pop()
    if current not in path:
      path.append(current)
      for child in reversed(graph[current]):
        if child not in path: stack.append(child)
  return path
    

graph = {1: [2, 3],
         2: [1, 4, 5, 6],
         3: [1, 4],
         4: [2, 3, 5],
         5: [2, 4, 6],
         6: [2, 5]}
         
# print dfs(graph,1)