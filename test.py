li = list(range(10))
print('li=',li)

print('li[2:8]=',li[2:8])
print('li[::-1]',li[::-1])





li = [i*2 for i in range(10)]
print('li = ',li)

li_2d = [ [0] * 3] *3
li_2d = [ [0] * 3  for i in range(3)]
print('li_2d = ',li_2d)
print('li_2d[0][0]=',li_2d[0][0])
li_2d[0][0] = 100
print('li_2d[0][0]=',li_2d[0][0])
print('li_2d = ',li_2d)

s = {x for x in range(10) if x % 2==0}
print(s)

d = {x:x%2==0 for x in range(10)}
print(d)
