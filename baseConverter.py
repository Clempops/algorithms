def baseConverter(digit, base):
  quotient = digit
  converted = []
  while quotient != 0:
    remainder = quotient % base
    quotient = quotient // base
    converted.insert(0, str(remainder))
    print converted

  return ''.join(converted)

print baseConverter(342, 10)