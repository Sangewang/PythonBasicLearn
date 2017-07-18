from __future__ import division
import string
from string import maketrans

class Demo:
  def isText(self,s):
    if not s:
      return True
    all_count  = len(s)
    text_count = 0
    #print 'The Length of %s is %d' % (s,all_count)

    for i in range(0,all_count):
      value = ord(s[i])
      if(0==value):
        return False
      #print "%s convert It's ASCII is %d" % (s[i],value)
      if(value>=32 and value<=126) or (value==8 or value==9 or value==10 or value==13):
        text_count+=1
        #print '%d -----> %d'%(value,text_count)
    #print 'text_count=%d count=%d'%(text_count,all_count)  
    percent = text_count/all_count
    #print 'The text percert is %d',percent
    if(percent>=0.7):
      return True
    else:
      return False

  def createStr(self,start,end):
    s = ''
    for i in range(start,end+1):
      s+=chr(i)
    #print s
    return s

A = Demo()
print "\"\" is a Text ? ==> ",A.isText("")
print "abcdefg is a Text ? ==> ",A.isText("abcdefg")
print "abcdefg\0 is a Text ? ==> ",A.isText("abcdegf\0") 
print "Special is a Text ? ==> ",A.isText("\n\n\0\n\n\0\n\n\n\0")
print "Special is a Text ? ==> ",A.isText("\r\n\t\b")

pStr = A.createStr(12,30)
print "createStr(12,30) is a Text ? ==> ",A.isText(pStr)

pStr = A.createStr(25,45)
print "createStr(25,45) is a Text ? ==> ",A.isText(pStr)





