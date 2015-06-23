def findPath(x, y, path):
  if x >= 0 and y >= 0:
    path.insert(0, (x, y))
    if x == 0 and y == 0:
      print path
    else:
      findPath(x-1, y, path)
      findPath(x, y-1, path)

findPath(3, 3, [])
    