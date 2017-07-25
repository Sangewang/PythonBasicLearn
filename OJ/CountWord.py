def CountWords(strLine):
  count = len(strLine)
  print 'The Length of strLine is ',count
  result = {'alpha':0,'space':0,'digit':0,'others':0}
  for i in xrange(count):
    if 'a'<=strLine[i]<='z' or 'A'<=strLine[i]<='Z':
      result['alpha'] += 1
    elif ' ' == strLine[i]:
      result['space'] += 1
    elif '\n' == strLine[i]:
      break
    elif '1'<=strLine[i]<='9':
      result['digit'] += 1
    else:
      result['others'] += 1

  return result

print CountWords('255.255.255.0\n is a ipv4 address')
print CountWords('255.255.255.a is not a ipv4 address.\n')
print CountWords('')
print CountWords("\0\n")


