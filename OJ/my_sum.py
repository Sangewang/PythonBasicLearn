def my_sum(i):
  if i<0 :
    raise ValueError
  elif i <= 1:
    return i
  else:
    return i + my_sum(i-1)


print(my_sum(1))
print(my_sum(100))
print(my_sum(500))
