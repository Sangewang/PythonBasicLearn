class Solution(object):
    def strStr(self, haystack, needle):
      haystack_lenth = len(haystack)
      needle_lenth   = len(needle)
      target_local = -1
      print("The Length of haystack is %d" % haystack_lenth)
      print("The Length of needle is %d" % needle_lenth)
      for i in xrange(haystack_lenth):
        print i
        tmp_i = i
        match = 0
        while(match < needle_lenth and tmp_i < haystack_lenth and haystack[tmp_i] == needle[match]):
           print needle[match]
           tmp_i += 1
           match += 1
        if(match == needle_lenth):
          target_local = i
          break
      return target_local

Test = Solution()
print Test.strStr('MyPython','Py')
