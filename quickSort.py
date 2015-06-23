def quicksort(seq):
    if len(seq) <= 1: 
        return seq
    lo, pi, hi = partition(seq)
    return quicksort(lo) + [pi] + quicksort(hi)

def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi
    
alist = [10, 1, 2, 3, 12, 4, 5, 11, 13, 15]
print quicksort(alist)