class Demo:
  def RemoveElement(self,nums,value):
    if not nums:
      return 0
    cnt = len(nums)
    flag = -1
    match = 0
    for i in range(cnt):
      if nums[i] == value:
        flag = i
        match+=1
      else:
        if flag != -1:
          nums[flag] = nums[i]
    result = match
    return result,nums

Test = Demo()
print Test.RemoveElement([1,2],1)
