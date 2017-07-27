class Demo:
  def findMyChar(self,inputStr):
    if not isinstance(inputStr,str):
      pass
    else:
      strLen  = len(inputStr)
      listStr = list(inputStr)
      for i in xrange(strLen):
        if listStr.count(inputStr[i])==1:
          return inputStr[i]
    return None

s = Demo()
print s.findMyChar('abaccdeff')
print s.findMyChar('')
print s.findMyChar(1234)
print s.findMyChar('adsfgfrdvasdgrd')

