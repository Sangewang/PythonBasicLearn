class Demo:
  def gcd(self,x,y):
    if x<=0 or y<=0:
      return None
    if x>=y:
      max_value = x
      min_value = y
    else:
      max_value = y
      min_value = x

    while(max_value % min_value):
      temp = max_value % min_value
      max_value = min_value
      min_value = temp
    return min_value

  def lcm(self,x,y):
    if x<=0 or y<=0 :
      return None
    return x * y / self.gcd(x,y)

test = Demo()
print test.gcd(2,9)
print test.lcm(2,9)

print test.gcd(84,24)
print test.lcm(84,24)

print test.gcd(0,9)
print test.lcm(24,0)
