A = '110101'
B = '111000'

def compareBits(A,B):
  if len(A) != len(B):
    if len(A) > len(B): return len(A)
    else: return len(B)
  else:
    i = 0
    found = False
    while not found and i <= len(A)-1:
      if int(A[i]) > int(B[i]): found = 'A'
      elif int(A[i]) < int(B[i]): found = 'B'
      i += 1
    print found

compareBits(A,B)