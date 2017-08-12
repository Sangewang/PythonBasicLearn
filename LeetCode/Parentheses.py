class Solution(object):
    def isValid(self, s):
      brauck ={'(':')','{':'}','[':']'}
      count = len(s)
      if count%2!=0 :
        return False
      for i in xrange(count):
        if i%2 != 0:
          i+=1
        if i == count:
          break
        if brauck[s[i]] != s[i+1]:
          return False
      return True
Test = Solution()
input = '()[]{}'
print Test.isValid(input)
input = '{[)}'

print Test.isValid(input)
