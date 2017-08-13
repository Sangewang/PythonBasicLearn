class Demo:
  def RemoveElement(self,nums,value):
    if not nums:
      return 0
    cnt = len(nums)
    flag_j = -1
    match = 0

    for i in range(cnt):
      if nums[i] == value:
        if i > flag_j:
          j = i+1
        else:
          j = flag_j+1
        while(j<cnt):
          if nums[j]!=nums[i]:
            nums[i] = nums[j]
            flag_j = j
          j+=1
    for i in range(cnt):
      if nums[i] != value:
        match+=1
      else:
        break
    return match,nums



Test = Demo()
print Test.RemoveElement([1,2],1)
print Test.RemoveElement([3,2,2,3],3)
print Test.RemoveElement([1,1],1)
print Test.RemoveElement([],1)
print Test.RemoveElement([1],1)
print Test.RemoveElement([2,2,3],2)
