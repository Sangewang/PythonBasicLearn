class Solution(object):
  def singleNumber(self,list):
    d_hash = {}
    result = -1
    for i in range(len(list)):
      if list[i] in d_hash:
        d_hash[list[i]] += 1
      else:
        d_hash[list[i]] = 1
    print('d_hash = ',d_hash)
    for (k,v) in d_hash.items():
      if v == 1:
        result = k
     
    return result

Test = Solution()
li_Single = [3,4,4,3,5,6,6,7,8,8,7]
print(Test.singleNumber(li_Single))
      
    
        
