class Demo:
  def TwoSum(self,num,target):
    result = []
    cnt = len(num)
    for i in range(cnt):
      left = target - num[i]
      temp = num[i]
      num[i] = '#'
      if left in num:
        j = num.index(left) 
        if i!=j and i<j:
          result.append(i)
          result.append(j)
      num[i] = temp
    return result


Test = Demo()
input = [3,3]
print Test.TwoSum(input,6)
        
    
