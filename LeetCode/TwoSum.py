class Demo:
  def TwoSum(self,num,target):
    result = []
    cnt = len(num)
    for i in range(cnt):
      left = target - num[i]
      if left in num:
        j = num.index(left) 
        if i!=j and i<j:
          result.append(i)
          result.append(j)
    return result


Test = Demo()
input = [1,2,7,9]
print Test.TwoSum(input,8)
        
    
