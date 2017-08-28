class Solution(object):
  def singleNumber(self,li):
    if not li:
      return -1
    result = li[0]
    for i in range(len(li)-1):
      result ^= li[i+1]
    return result
Test = Solution()
li_Single = [3,4,4,3,5,6,6,7,8,8,7]
print(Test.singleNumber(li_Single))
      
    
        
