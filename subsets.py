def subsets(myset):
  subsets = [set()]
  for x in myset:
    news = []
    for y in subsets:
      new = y.copy()
      new.add(x)
      news.append(new)
    for new in news:
      subsets.append(new)
  return subsets
  
print subsets(set(range(3)))