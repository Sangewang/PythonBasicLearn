class Solution(object):
  def CreateAMatrix(self,m,n):
    li_2d = [i for i in range(m)]
    print(li_2d)
    for i in range(m):
      li_2d[i] = [j for j in range(i*n+1,(i+1)*n+1)]
    return li_2d
   
  def SumMatrix(self,li_2d):
    Sum_li = li_2d
    print('Sum_li=',Sum_li)
    m = len(li_2d)
    n = len(li_2d[0])
    sum = 0
    for i in range(m):
      for j in range(n):
        sum += li_2d[i][j]
        Sum_li[i][j] = sum
    return Sum_li
Test = Solution()
Matrix_A = Test.CreateAMatrix(3,4)
print('Matrix_A=',Matrix_A)
Matrix_B = Test.SumMatrix(Matrix_A)
print('Matrix_B=',Matrix_B)

