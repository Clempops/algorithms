A = 'hello'
B = 'hello'

def compareString(A, B):
  if abs(len(A)  - len(B)) != 0:
    return False
  else:
    hashTable = [0] * len(A)
    for i in range(len(A) - 1):
      hashed_pos = hashValue(A[i], len(A))
      add(hashed_pos, hashTable, 1)
      hashed_pos = hashValue(B[i], len(A))
      add(hashed_pos, hashTable, -1)
    if hashTable != ([0] * len(A)): return False
    else: return True
    
def hashValue(key, length):
  return ord(key) % length

def add(hashed_pos, hashTable, i):
  if hashTable[hashed_pos] == None:
    hashTable[hashed_pos] = i
  else: hashTable[hashed_pos] += i
  
print compareString(A, B)