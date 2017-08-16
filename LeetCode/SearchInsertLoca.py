class Solution(object):
    def searchInsert(self, nums, target):
      try:
        loca = nums.index(target)
      except ValueError:
        nums.append(target)
        nums.sort()
        loca = nums.index(target)
      finally:
        return loca

Test = Solution()
nums = [1,3,5,6]
print(Test.searchInsert(nums,5))
print(Test.searchInsert(nums,2))
