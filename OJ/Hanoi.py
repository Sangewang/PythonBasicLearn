def hanoi(n,source,target,helper):
  if n == 1:
    print(source + '->' + target)
  else:
    hanoi(n-1,source,helper,target)
    print(source + '->' + target)
    hanoi(n-1,helper,target,source)

hanoi(4,'A','B','C')

