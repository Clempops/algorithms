def decrease(A, k):
  i = 1
  while (A >> i) > 0:
    A >> i
    i += 1
  mask = 1 << i
  while mask > 0 and k > 0:
    if A & mask != 0:
      A &= ~mask
      k -= 1
    mask >>= 1
  return A

print decrease(1203, 4)
    