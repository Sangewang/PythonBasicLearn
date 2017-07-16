def factorial(n):
  if n==1:
    return 1
  else:
    return n*factorial(n-1)

num = input("Please Enter a Num:")
print "The Fact N is =",factorial(num)



def power(x,n):
  if n==0:
    return 1
  else:
    return x*power(x,n-1)

num   = input("Please Enter a Num:")
index = input("Please Enter a Index:")
print "The Power of x**n is =",power(num,index)
