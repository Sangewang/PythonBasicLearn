class Solution(object):
  def merge(self, nums1, m, nums2, n):
    i = n-1
    count = 0
    flag = 0
    while(i>=0 and i<n):
      flag = 0
      j = m+count-1
      print('i=',i,'j=',j)
      while(j>=0 and j<m+count):
        if nums2[i]>nums1[j]:
          nums1.insert(j+1,nums2[i])
          flag = 1
          count+=1
          break;
        else:
          j-=1
      if flag == 0:
        nums1.insert(0,nums2[i])
      i-=1
    nums1 = nums1[:m+n]  
    return nums1
Test = Solution()
nums1 = [1,3,5,7,9,11,13,15]
nums2 = [2,4,6,8,10,12,14,16]
print(Test.merge(nums1,5,nums2,5))

nums1 = [0]
nums2 = [1]
print(Test.merge(nums1,0,nums2,1))
