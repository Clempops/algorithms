def drawLines(allbytes, width, x1, x2):
  first_byte = x1 // 8
  last_byte = x2 // 8
  
  for i in allbytes[first_byte:last_byte_mask+1]:
    i = 0xFF
  
  first_byte_mask = 0xFF >> (x1 % 8)
  last_byte_mask = 0xFF << (8 - (x2 % 8))
  
  allbytes[first_byte] |= first_byte_mask
  allbytes[last_byte] |= last_byte_mask