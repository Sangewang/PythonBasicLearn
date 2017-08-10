import math
class Demo:
  def Palindrom(self,input):
    if input>pow(2,31)-1 or input < 0:
      return False
    len = 1
    while(input/len>=10):
      len *= 10
    while(input):
      if input%10 != input/len:
        return False
      else:
        input = (input%len)/10
        len = len/100
    return True

Test = Demo()
print Test.Palindrom(1221)
print Test.Palindrom(0)
print Test.Palindrom(-1)
print Test.Palindrom(12321)
print Test.Palindrom(1111111111111111)
print Test.Palindrom(12)
    
