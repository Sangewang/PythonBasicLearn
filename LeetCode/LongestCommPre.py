class Demo:
  def GetTheCommon(self,str1,str2):
    '''str1 = str1[::-1]
    str2 = str2[::-1]'''
    print('The first string is = ',str1)
    print('The second string is = ',str2)
    common_len = 0
    if len(str1) <= len(str2):
      count = len(str1)
    else:
      count = len(str2)
    print('The min length is = ',count)
    for i in xrange(count):
      print('str1[%d] = %s'%(i,str1[i]))
      print('str2[%d] = %s'%(i,str2[i]))
      if str1[i] == str2[i]:
        common_len = i+1
      else:
        break
    print("The common len is = ",common_len)
    print("The Common Str is = ",str1[:common_len])


  def LongestCommonPref(self,input):
    if input == []:
      return ""
    print("Before sort = ",input)
    '''sorted(input)'''
    input.sort()
    print("After  sort = ",input)
    count = len(input)
    print("The length of input is = ",count)
    self.GetTheCommon(input[0],input[count-1])
  

input = []
Test = Demo()
Test.LongestCommonPref(input)
    
