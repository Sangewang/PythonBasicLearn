class Demo:
  def RemoveDuplicate(self,nums):
    if not nums:
      return []       
    if len(nums) == 1:
      return nums
    flag = nums[0] - 1
    cnt = len(nums)
    flag_cnt = 0
    for i in xrange(cnt-1):
      if nums[i] == nums[i+1]:
        flag_cnt+=1
        nums[i] = flag
        nums.sort()
    return nums[flag_cnt:cnt]
Test = Demo()
print Test.RemoveDuplicate([1,2,2,3,3,4,4,5])
print Test.RemoveDuplicate([])
print Test.RemoveDuplicate([1,1,2])
