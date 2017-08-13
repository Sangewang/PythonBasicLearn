class Solution(object):
    def mergeTwoLists(self, l1, l2):
      merge = []
      if len(l1) == 0 and len(l2) == 0:
        pass
      else:
        merge = l1 + l2
        merge.sort()
      return merge
Test = Solution()

l1 = []
l2 = []
print Test.mergeTwoLists(l1,l2)
