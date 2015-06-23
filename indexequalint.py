def findIndexInt(alist):
  first  = 0
  last = len(alist) - 1
  while first <= last:
    mid = (first + last) // 2
    if mid == alist[mid]:
      return mid
    if mid > alist[mid]:
      first = mid + 1
    elif mid < alist[mid]:
      last = mid - 1
  return False

alist = [-3,-1,1,3,6]
print findIndexInt(alist)