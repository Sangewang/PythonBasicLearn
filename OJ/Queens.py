def conflict(state,nextX):
  nextY = len(state)
  print 'nextX=',nextX, 'nextY= ',nextY,'range(nextY)=',range(nextY)
  for i in range(nextY):
    
    print i,state[i]
    if abs(state[i]-nextX) in (0,nextY-i):
      print 'Error,i=',i
      return True
  return False

def queens(num,state):
  if len(state) == num-1:
    for pos in range(num):
      if not conflict(state,pos):
        yield pos

print list(queens(4,(1,3,0)))
