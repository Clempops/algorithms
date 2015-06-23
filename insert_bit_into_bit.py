N = 10000000000
M = 10011

def insert_M_into_N(N, M, i, j):
  M = list(str(M))
  N = list(str(N))
  for x in range(len(N)-i-1, len(N)-j-2, -1):
    print N
    N[x] = M.pop()
  print ''.join(N)
insert_M_into_N(N, M, 2, 6)