def FibN(num):
  'Calculate Fib Sequency.'
  result = [0,1]
  while(num<=0):
    num = input('How Many Fib Do You Want Get:')
  if num == 1:
    result = [0]
  for i in range(num-2):
    result.append(result[-2]+result[-1])
  return result

num = input('How Many Fib Do You Want Get:')
print FibN(num)
