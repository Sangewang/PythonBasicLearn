class Solution(object):
  def CountAndSay(self, n):
    if n == 1:
      return "1"
    if n == 2:
      return "11"
    result = self.CountAndSay(n-1)
    cnt = len(result)
    s = ""
    for i in range(cnt-1):
      count = 1 
      if result[i] == result[i+1]:
        count+=1
      s = s + str(count) + result[i]
      if(result[cnt-1]!=result[cnt-2]):
        s = s + str(1) + result[cnt - 1]
    return s


Test = Solution()

print(Test.CountAndSay(1))
print(Test.CountAndSay(2))
print(Test.CountAndSay(3))
print(Test.CountAndSay(4))
print(Test.CountAndSay(5))
print(Test.CountAndSay(6))
print(Test.CountAndSay(7))
print(Test.CountAndSay(8))
print(Test.CountAndSay(9))

