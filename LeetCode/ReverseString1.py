class Solution(object):
  def swap(self,str_list,start,end):
    print(start,end)
    while(start<end):
      str_list[start],str_list[end] = str_list[end],str_list[start]
      start+=1
      end -= 1
  
  def reverseString(self, s):
    str_list = list(s)
    i = 0
    '''
    while(i<len(str_list)):
      if str_list[i] != ' ':
        j = i
        while(j<len(str_list) and str_list[j]!=' '):
          j+=1
        self.swap(str_list,i,j-1)
        i=j
      else:
        i+=1
    '''
    self.swap(str_list,0,len(str_list)-1)
    return ''.join(str_list)

Test = Solution()
print(Test.reverseString('I love Chnia!!'))

