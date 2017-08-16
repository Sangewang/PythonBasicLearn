class Solution(object):
    def searchInsert(self, nums, target):
      cnt = len(nums)
      start = 0
      end   = cnt-1
      while(start < end):
        mid = (end + start)//2
        if nums[mid] == target:
          return mid
        else:
          if nums[mid] > target:
            end = mid
          else:
            start = mid + 1
      return start
 
Test = Solution()
nums = [1,3,5,6]
print(Test.searchInsert(nums,5))
print(Test.searchInsert(nums,2))
