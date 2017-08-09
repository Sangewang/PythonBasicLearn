class Demo:
  def AddDiffSum(self,input):
    result = 0
    store  = []
    for i in input:
      if store.count(i) == 0:
        store.append(i)
    for j in store:
      result += j
    return result

Test = Demo()
print Test.AddDiffSum([1,1,2,3])
