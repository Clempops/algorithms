string = 'hello'

def removeDuplication(string):
  res = ''
  for i in string:
    if i not in res:
      res += i
  return res
  
print removeDuplication(string)
    