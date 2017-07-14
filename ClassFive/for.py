words = ['This','is','an','ex','parrot']
for word in words:
  print word


numbers = [0,1,2,3,4,5,6,7,8,9]
for index in numbers:
  print index

for key in range(0,101):
  if key%3==0:
    print key

d = {'x':1,'y':2,'z':3}
for key in d:
  print key,'corresponds to',d[key]

for key,value in d.items():
  print key,'corresponds to',value
