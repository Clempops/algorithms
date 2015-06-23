def switchBits(A):
  even = A & 0xAAAAAAAA
  odd = A & 0x55555555
  even = even >> 1
  odd << 1
  return even | odd
  
print switchBits(12)