from random import *
num   = input('How Many dice? ')
sides = input('How Many sides per die? ')
sum   = 0
for i in range(num):
  sum += randrange(sides)+1
print 'The Result is ',sum
