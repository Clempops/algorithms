##### LIGHT VERSION

class Heap:
  def __init__(self):
    self.list = [0]
    self.size = 0
    
  def build(self, alist):
    self.size = len(alist)
    self.list = self.list + alist
    i = self.size // 2
    while i > 0:
      self.sortDown(i)
      i -= 1
      
  def sortDown(self, i):
    if self.size > i*2:
      childpos = self.mini(i)
      if self.list[childpos] < self.list[i]:
        t = self.list[childpos]
        self.list[childpos] = self.list[i]
        self.list[i] = t
        self.sortDown(childpos)
    
  def mini(self, i):
    if i*2 > self.size:
      if self.list[i*2] < self.list[i*2+1]:
        return i*2
      else:
        return i*2+1
    else:
      return i*2

heap = Heap()
heap.build([9,6,10,8,12])

print heap.list

##### COMPLETE VERSION

class Heap:
  def __init__(self):
    self.list = [0]
    self.size = 0
    
  def sortUp(self, item):
    found = False
    i = self.size
    while not found:
      if item < self.list[i // 2]:
        t = self.list[i // 2]
        self.list[i // 2] = item
        self.list[i] = t
        found = True
      i = i // 2

  def findMinChild(self, i):
    if self.size < i*2+1:
      child = i*2
    else:
      right = self.list[i*2+1]
      left = self.list[i*2]
      if right >= left: child = i*2
      else: child = i*2+1
    return child
    
  def sortDown(self, item):
    i = item
    while i*2 <= self.size:
      child = self.findMinChild(i)
      if self.list[child] < self.list[i]:
        t = self.list[i]
        self.list[i] = self.list[child]
        self.list[child] = t
      i = child

  def build(self, alist):
    self.list = [0] + alist
    self.size = len(alist)
    i = self.size // 2
    while i > 0:
      self.sortDown(i)
      i -= 1

  def insert(self, item):
    self.list.append(item)
    self.sortUp(item)
    self.size += 1

  def findMin(self):
    return self.list[1]

  def delMin(self):
    self.list[1] = self.list[-1]
    self.sortDown(1)
    self.list.pop()
    self.self -= 1


heap = Heap()
heap.build([9,6,10,8,12])

print heap.list
