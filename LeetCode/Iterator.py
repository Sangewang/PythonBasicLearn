from collections import Iterable
from collections import Iterator

print(isinstance([1,2,3],Iterable))
print(isinstance([1,2,3],Iterator))
print(isinstance({},Iterable))
print(isinstance(123,Iterable))
print(isinstance('abc',Iterable))

g = (x * x for x in range(10))
print(type(g))
print(isinstance(g,Iterable))
print(isinstance(g,Iterator))

for i in g:
  print(i)


