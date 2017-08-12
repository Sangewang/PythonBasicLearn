class Solution(object):
    def isValid(self, s):
      left = ['(','[','{']
      right = [')',']','}']
      match = {')':'(',']':'[','}':'{'}
      result = []
      count = len(s)
      for i in xrange(count):
        if s[i] in left:
          result.append(s[i])
        if s[i] in right:
          if len(result)!=0 and match[s[i]]==result[-1]:
            result.pop()
          else:
            return False
      if len(result) == 0:
        return True
      else:
        return False
Test = Solution()
input = '()[]{}'
print Test.isValid(input)
input = ")["
print Test.isValid(input)
input = ")"
print Test.isValid(input)
input = ""
print Test.isValid(input)
