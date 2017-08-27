class Solution(object):
  def reverseBits(self,n):
    li = [0] * 32
    count = 0
    num = 0
    while(n!=0):
      li[31-count] = n%2
      n = n//2
      print('n=',n)
      count+=1
    print(li)
    li.reverse()
    print(li)
    for i in range(32):
      num += pow(2,31-i) * li[i]
    return num
Test = Solution()
print(Test.reverseBits(5))
print(Test.reverseBits(10))
print(Test.reverseBits(43261596))
    
