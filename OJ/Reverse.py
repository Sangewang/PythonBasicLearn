import math
class Demo:
  def ReverseInt(self,input):
    
    result = []
    output = []
    sum = 0
    if input<0:
      index = 0
      input = 0 - input
    else:
      index = 1
    if input > pow(2,32):
      return 0
    str_input = str(input)
    result = list(str_input)
    count = len(result)
    
    for i in range(count):
      output.insert(0,int(result[i]))
      sum += pow(10,count-i-1) * int(result[count-1-i]) 
    
    if index == 0:
      sum = 0 - sum
    print str_input
    print result
    print output
    print sum
     
num =  pow(2,32)
Test = Demo()
Test.ReverseInt(123)
Test.ReverseInt(-123)
print Test.ReverseInt(0-num-1)
