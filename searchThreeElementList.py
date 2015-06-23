def searchThreeElements(alist):
  res = [alist[0]]
  for i in alist[1:]:
    if len(res) >= 3: return res
    if i > res[-1]: res.append(i)
  return False 

print searchThreeElements([1, 2, 0, 4, 5, 6])