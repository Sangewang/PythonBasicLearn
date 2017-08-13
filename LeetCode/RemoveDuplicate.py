class Demo:
  def RemoveDuplicate(self,array):
    if len(array)==0 or len(array) == 1:
      return array
    flag = array[0] - 1
    cnt = len(array)
    flag_cnt = 0
    for i in xrange(cnt-1):
      if array[i] == array[i+1]:
        flag_cnt+=1
        array[i] = flag
    array.sort()
    return array,cnt-flag_cnt,array[flag_cnt:cnt]

Test = Demo()
print Test.RemoveDuplicate([1,2,2,3,3,4,4,5])
print Test.RemoveDuplicate([])
