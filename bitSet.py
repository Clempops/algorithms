class BitSet32():
 def __init__(self, size):
   self.bitset = [0] * (size // 32 + 1)

 def get(self,pos):
   wordNumber = pos >> 5
   bitNumber = pos & 0x1F
   return (self.bitset[wordNumber] & (1 << bitNumber) ) == 1

 def set(self,pos):
   wordNumber = pos >> 5
   bitNumber = pos & 0x1F
   self.bitset[wordNumber] |= 1 << bitNumber

#######

class BitSet8():
 def __init__(self, size):
   self.bitset = [0] * (size // 8 + 1)

 def get(self,pos):
   wordNumber = pos >> 3
   bitNumber = pos & 0x3
   return (self.bitset[wordNumber] & (1 << bitNumber) ) == 1

 def set(self,pos):
   wordNumber = pos >> 3
   bitNumber = pos & 0x3
   self.bitset[wordNumber] |= 1 << bitNumber