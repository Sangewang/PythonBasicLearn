class Solution(object):
    def mergeTwoLists(self, l1, l2):
      merge = l1 + l2
      merge.sort()
      print merge
Test = Solution()

l1 = []
l2 = []
Test.mergeTwoLists(l1,l2)
