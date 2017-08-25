class Solution(object):
  def hammingWeight(self,n):
    count = 0
    while(n!=0):
      count+=1
      n = n & (n-1)
    return count
Test = Solution()
print(Test.hammingWeight(5))
print(Test.hammingWeight(11))
print(Test.hammingWeight(1))
