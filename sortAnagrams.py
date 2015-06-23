A = ['abz', 'efb', 'azb', 'feb', 'zba', 'bfe']
B = ['a', 'b', 'b', 'a', 'c', 'c']

def quicksort(seq):
  if len(seq) <= 1: 
    return seq
  left, right, pi = partition(seq)
  return quicksort(left) + right + pi

def partition(seq):
  pi, seq = seq[0], seq[1:]
  left = [x for x in seq if sorted(x) != sorted(pi)]
  right = [x for x in seq if sorted(x) == sorted(pi)]
  return left, right, [pi]
    
print quicksort(A)