class Demo:
  def demo(self,s):
    x = list()
    if type(s) is not list:
      raise
    elif len(s) == 0:
      pass
    else:
      for i in xrange(len(s)):
        if x.count(s[i]) == 0:
          x.append(s[i])
    return x


test = Demo()
s = [1,'11',22,'22',3,'22',3,'11',4,5,5,2,'33','11']
print test.demo(s)
