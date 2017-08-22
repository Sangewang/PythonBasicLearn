class Solution(object):
  def countPrimes(self, n):
    count = 0
    result = []
    if n<2:
      return count
    
    for i in range(2,n):
      upper = int(pow(i,0.5)) + 1
      
      flag = 0
      for j in range(2,upper):
        if i%j == 0:
          flag = 1
          break
      if(flag == 0 ):
        count+=1
        result.append(i)
    return count,result
Test = Solution()
print(Test.countPrimes(100000))
