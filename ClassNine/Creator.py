def flatten(nested):
  try:
     try:nested+''
     except TypeError:pass
     else:raise TypeError
     for sublist in nested:
      for element in sublist:
        yield element
  except TypeError:
    yield nested

nested = [[1,2],[3,4],[5]]
for num in flatten(nested):
  print num*2


