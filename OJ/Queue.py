class Solution(object):
  def push(self,li,data):
    li.append(data)
    return li
  def top(self,li):
    if len(li) == 0:
      return 'Empty Queue'
    return li[0]
  def pop(self,li):
    if len(li) == 0:
      return 'Empty Queue'
    return li.pop(0)
  def show(self,li):
    return li
Queue = Solution()
li = []
print(Queue.push(li,5))
print(Queue.push(li,4))
print(Queue.push(li,3))
print(Queue.push(li,2))
print(Queue.push(li,1))
print(Queue.top(li))    
print(Queue.pop(li))    
print(Queue.show(li))
