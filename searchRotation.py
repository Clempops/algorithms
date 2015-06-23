def searchByRotation(alist, item):
	i = 0
	while i <= len(alist):
		temp = alist.pop()
		if temp == item: return True
		alist.insert(0, temp)
		i += 1
	return False

print searchByRotation(range(10), 53)