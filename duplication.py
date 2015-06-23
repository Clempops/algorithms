string = 'helo'
pool = []

def duplication(string, pool):
  for i in string:
    if i in pool:
      return False
    else:
      pool.append(i)
  return True

print duplication(string, pool)
