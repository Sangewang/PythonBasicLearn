def checkIPv4(ipStr):
  print '+++++++++++++++++++++++++++++++++++++++'
  print 'The Input Ip String is =',ipStr
  IPv4List  = ipStr.split('.')
  print 'Ip String convert to ip List is =',IPv4List
  IPv4Count = len(IPv4List)
  print 'The Num of IPv4List is =',IPv4Count

  if(4!=IPv4Count):
    return False

  for i in range(0,IPv4Count):
    Each_IPv4_List_Len = len(IPv4List[i])
    print IPv4List[i],Each_IPv4_List_Len
    if Each_IPv4_List_Len < 1 or Each_IPv4_List_Len > 3:
      print "Error: The Len of %s is %d" % (IPv4List[i],Each_IPv4_List_Len)
      return False
    
    for j in range(0,Each_IPv4_List_Len):
      if IPv4List[i][j]<'0' or IPv4List[i][j]>'9':
        print "Error: The %s is not only number" % IPv4List[i]
        return False

    value_of_each_IPv4_List = int(IPv4List[i])
    if(value_of_each_IPv4_List<0 or value_of_each_IPv4_List>255):
      print "The Number of %s is overflow" % IPv4List[i]
      return False

  if int(IPv4List[0]) == 0:
    if int(IPv4List[1])==0 and int(IPv4List[2])==0 and int(IPv4List[3])==0 :
      pass
    else:
      print "Error: Not all is Zero"
      return False

  return True
    
print checkIPv4("192.168.1.1")
print checkIPv4("0.0.0.0")
print checkIPv4("255.255.255.255")
print checkIPv4("1.2.3.a")
print checkIPv4("1231.231.3.4")
print checkIPv4("0.1.1.1")

