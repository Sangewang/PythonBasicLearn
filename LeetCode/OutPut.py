class Solution(object):
  def InitAList(self,m,n):
    if m<=0 or n<=0 :
      return list_mn  
    list_mn = [i for i in range(m)]
    for i in range(m):
      list_mn[i] = [j for j in range(i*n,(i+1)*n)] 
    return list_mn
  
  def OutPutList(self,list_2d,m,n):
    print('int(m+1)/2=',int((m+1)/2))
    result = []
    if m == 1 and n==1:
      result.append(0)
    for i in range(int((m+1)/2)):
      print('i=',i)
      temp_i = i
      temp_j = i
      print('line1------------------------------------------')
      while(temp_j>=0 and temp_j<n-i-1):
        print(list_2d[temp_i][temp_j])
        result.append(list_2d[temp_i][temp_j])
        temp_j+=1
      
      print('line2------------------------------------------')
      while(temp_i>=0 and temp_i<m-i-1):
        print(list_2d[temp_i][temp_j])
        result.append(list_2d[temp_i][temp_j])
        temp_i+=1
     
      
      print('line3------------------------------------------')
      while(temp_j>=i+1 and temp_j<n-i):
        print(list_2d[temp_i][temp_j])
        result.append(list_2d[temp_i][temp_j])
        temp_j-=1
      print('line4------------------------------------------')
      while(temp_i>=i+1 and temp_i<m-i and temp_i!=temp_j):
        print(list_2d[temp_i][temp_j])
        result.append(list_2d[temp_i][temp_j])
        temp_i-=1
    return result      
  
Test = Solution()
list_2d = Test.InitAList(1,1)
print(list_2d)
print(Test.OutPutList(list_2d,1,1))
