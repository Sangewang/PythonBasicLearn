def fid(n):
  if n<0:
    return 0
  li = [1,1]
  for i in range(2,n+1):
    li.append(li[i-1]+li[i-2])
  return li[n]


print(fid(10))
