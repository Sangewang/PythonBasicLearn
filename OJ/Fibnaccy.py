def fid(n):
  if n == 1 or n == 2:
    return 1
  else:
    return fid(n-1) + fid(n-2)

print(fid(1))
print(fid(2))
print(fid(3))
print(fid(4))
print(fid(5))
print(fid(6))
