class Solution(object):
  def countPrimes(self, n):
    count = 0
    result = []
    output = []
    if n<2:
      return count
    result = list(range(0,n))
    upper = int(pow(n,0.5))
    for i in range(2,n):
      if result[i]:
        j = i * i
        while(j < n):
          result[j] = 0
          j+=i
    for i in range(2,n):
      if result[i] != 0:
        count+=1
        output.append(result[i])
    return count

Test = Solution()
print(Test.countPrimes(100000))
