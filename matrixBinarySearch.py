def binarySearchMatrix(matrix, item):
  if len(matrix) == 0: print 'Error'
  else:
    mid_height = len(matrix) // 2
    mid_width = len(matrix[0]) // 2
    mid = matrix[mid_height][mid_width]
    if item > mid:
      matrix = matrix[mid_height+1:]
      for i in range(len(matrix)):
        matrix[i] = matrix[i][:mid_width+1]
      print matrix
      binarySearchMatrix(matrix, item)
    elif item < mid:
      matrix = matrix[:mid_height]
      for i in range(len(matrix)):
        matrix[i] = matrix[i][mid_width:]
      print matrix
      binarySearchMatrix(matrix, item)
    else: print 'Found'
      

matrix = [[0 for x in range(3)] for x in range(3)]
matrix[0][0] = 15
matrix[0][1] = 20
matrix[0][2] = 40
matrix[1][0] = 20
matrix[1][1] = 35
matrix[1][2] = 80
matrix[2][0] = 30
matrix[2][1] = 55
matrix[2][2] = 95

print matrix
binarySearchMatrix(matrix, 35)
