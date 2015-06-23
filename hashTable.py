class HashTable:

  def __init__(self):
    self.size = 11
    self.slots = [None] * self.size
    self.data = [None] * self.size
    
  def hash(self, key):
    hashValue = key % len(self.slots)
    return hashValue
    
  def rehash(self, hashValue):
    rehashValue = (hashValue + 1) % len(self.slots)
    return rehashValue
  
  def __getitem__(self,key):
    position = self.hash(key)
    found = False
    if self.slots[position] == None:
      return None
    else:
      while found == False:
        if self.slots[position] == position:
          found = True
        else:
          position = rehash(position)
      return self.data[position]

  def __setitem__(self, key, value):
    position = self.hash(key)
    emptyFound = False
    while not emptyFound:
      if self.slots[position] == None:
        emptyFound = True
        self.slots[position] = key
        self.data[position] = value
        # fill
      elif self.slots[position] == key:
        emptyFound = True
        self.data[position] = value
      else:
        position = self.rehash(position)
    
    return True
    
  def len(self):
    length = 0
    for key in collection.slots:
      if key != None: length += 1
    return length

# 

collection = HashTable()

collection[1] = 'word1'
collection[2] = 'word2'
collection[3] = 'word3'
collection[4] = 'word4'
collection[5] = 'word5'