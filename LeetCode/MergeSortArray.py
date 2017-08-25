class Solution(object):
  def merge(self, nums1, m, nums2, n):
    print('nums1 = ',nums1)
    nums1.extend(nums2) 
    print('nums1 = ',nums1)
    return sorted(nums1)
    #print('nums1 = ',nums1)
    #return nums1
Test = Solution()
nums1 = [10,8,6,4,2]
nums2 = [9,7,5,3,1]
print(Test.merge(nums1,5,nums2,5))
