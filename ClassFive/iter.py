names = ['anne','beth','geory','damon']
ages  = [12,45,32,102]
for i in range(len(names)):
  print names[i],'is',ages[i],'years old'


for name,age in zip(names,ages):
  print name,'is',age,'years old'
