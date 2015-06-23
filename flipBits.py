def flipBits(A, B):
  xor = "{0:b}".format(A ^ B)
  t = 0
  for i in str(xor): t += int(i)
  return t

print flipBits(29, 15)