# def binarySearch(alist, item):
#   if len(alist) == 0:
#     return False
#   else:
#     mid = len(alist) // 2
#     if alist[mid] == item:
#       return True
#     else:
#       if item < alist[mid]:
#         return binarySearch(alist[:mid],item)
#       else:
#         return binarySearch(alist[mid+1:],item)
#
# print binarySearch([1,2,4,5], 5)

#######

def binarySearch(alist, item):
  first = 0
  last = len(alist)-1
  while first <= last:
    midpoint = (first + last) // 2
    if alist[midpoint] == item:
      return True
    else:
      if item < alist[midpoint]:
        last = midpoint-1
      else:
        first = midpoint+1
  return False
  
print binarySearch([1,2,4,5], 5)