string = 'hello'

def reverseRecursion(string, res):
  if string != '':
    res += string[-1]
    return reverseRecursion(string[:-1], res)
  else:
    return res
  
print reverseRecursion(string, '')