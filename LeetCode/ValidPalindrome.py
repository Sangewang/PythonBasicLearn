class Solution(object):
  def __init__(self,pstr):
    print('Solution Init....')
    self.pstr = pstr

class Judge(Solution):
  def filter_str(self,pstr):
    result = []
    for i in pstr:
      if i.isdigit() or i.isalpha():
        result.append(i.lower())
    return result
  def ValidPalindrome(self):
    pstr = self.pstr
    result = self.filter_str(pstr)
    print('result = ',result)
    judge = 0
    left   = 0
    right  = len(result)-1
    while(left<right):
      if result[left]!=result[right]:
        judge = 1
        break
      else:
        left+=1
        right-=1
    if judge == 1:
      return False
    else:
      return True


if __name__ == "__main__":
  Test = Judge("A man, a plan, a canal: Panama")
  print(Test.ValidPalindrome())
