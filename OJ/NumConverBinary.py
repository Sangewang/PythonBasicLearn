class Demo:
  def binary(self,n):
    if n==0:
      return '0'
    result = []
    while(n):
      m = str(n%2)
      result.insert(0,m)
      n /= 2

    return ''.join(result)

A = Demo()
print A.binary(255)
print A.binary(25)
print A.binary(10)
print A.binary(0)








