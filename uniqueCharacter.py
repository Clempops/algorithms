def hash(l):
  hashValue = ord(l) % 5
  return hashValue

string = 'hello'
hashTable = [None] * 5

for l in string:
  hashed = hash(l)
  if hashTable[hashed] != None: found = True
  else: hashTable[hashed] = l 
print found