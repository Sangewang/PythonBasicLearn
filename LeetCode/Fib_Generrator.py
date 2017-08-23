import traceback
def Fib_Generator(limit):
  try:
    n,a,b = 0,0,1
    while(n<limit):
      yield b
      a,b = b,a+b
      n += 1
    return 'done'
  except StopIteration:
    print("Have Been End")
    pass
    
f = Fib_Generator(5)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
try:
  print(next(f))
except StopIteration:
  pass
  
