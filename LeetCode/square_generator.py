li = []
for i in range(1000000):
  li.append(i*i)

for i in range(10):
  print(li[i])


print('---------------------------------------------------------------------------')
li_generator = (x * x for x in range(1000000))
for i in range(10):
  print(next(li_generator))
