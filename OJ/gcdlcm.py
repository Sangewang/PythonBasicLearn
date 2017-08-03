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
print 'The gcd(2,9) is = ',test.gcd(2,9)
print 'The lcm(2,9) is = ',test.lcm(2,9)

print 'The gcd(84,24) is = ',test.gcd(84,24)
print 'THe lcm(84,24) is = ',test.lcm(84,24)

print 'The gcd(0,9) is = ',test.gcd(0,9)
print 'THe lcm(24,0) is = ',test.lcm(24,0)
