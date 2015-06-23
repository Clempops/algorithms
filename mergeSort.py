def mergeSort(alist):

  if len(alist) > 1:
    middle = len(alist) // 2
    left = alist[:middle]
    right = alist[middle:]
    
    # left and right are not sorted, lets do it:

    mergeSort(left)
    mergeSort(right)
    
    sort(alist, left, right)

def sort(alist, left, right):
  l = 0
  r = 0
  k = 0
  
  while l < len(left) and r < len(right):
    # need comparison to fill
    if left[l] < right[r]:
      alist[k] = left[l]
      l += 1
    else:
      alist[k] = right[r]
      r += 1
    k += 1
    
  while l < len(left):
    # fill rest of left
    alist[k] = left[l]
    l += 1
    k += 1
    
  while r < len(right):
    # fill rest of right
    alist[k] = right[r]
    r += 1
    k += 1
  

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print alist
