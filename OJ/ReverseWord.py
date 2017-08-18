class Demo(object):
  def swap(self,str,start,end):
    str_t = str.split()
    print(str_t)
      
    while(start < end):
      temp = str_t[start]
      str_t[start] = str_t[end]
      str_t[end] = temp
      strt += 1
      end -= 1
    return str
  def Reverse(self,str):
    cnt = len(str)
    left = 0
    right = cnt - 1
    self.swap(str,left,right)
    print(str)
    for i in len(cnt):
      if not str[i]:
        start = i
        step = i
        while(str[step]!=' '):
          step+=1
        end = step
        self.swap(str,start,end)
        i = end + 1
    return str


Test = Demo()
str = "I love China !!"
print(Test.Reverse(str))
    
