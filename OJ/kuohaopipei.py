'''
Description: Check() is Balance
Input      : string s
OutPut     : None
Return     : Bool,True/False
'''

class Demo:
  def demo(self,s):
    strLen = len(s)
    stack  = []
    for i in xrange(strLen):
      if s[i] == '(':
        stack.append(s[i])
      else:
        if s[i] == ')':
          if len(stack) > 0:
            stack.pop()
          else:
            return False
        else:
          pass
    if len(stack)>0:
      return False
    return True

Test = Demo()
print Test.demo('1*(2 + 3)')
print Test.demo(')(+2)')
print Test.demo('(()()())')
