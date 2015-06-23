def permutation(string):
  compute(string, [])
  
def compute(string, letters):
  if letters == []:
    for letter in string:
      compute(letter, string.replace(letter,''))
  else:
    if letters != '':
      for index, letter in enumerate(letters):
        compute(string + letter, letters.replace(letter, ''))
    else:
      print string
    
permutation('salut')