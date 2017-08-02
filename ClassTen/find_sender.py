import fileinput,re
pat = re.compile('From: (.*) <.*?>$')
for line in fileinput.input():
  m = pat.match(line)
  if m:
    print 'Find The Target Line: ',m.group(0)
    print 'Find The Sender: ',m.group(1)

print '\n'
pat = re.compile(r'[a-z\-\.]+@[a-z\-\.]+',re.IGNORECASE)
addresses =  set()
for line in fileinput.input():
  for address in pat.findall(line):
    addresses.add(address)

print 'Find The Email All Address: '
for address in sorted(list(addresses)):
  print address

'''
adds = []
for i in addresses:
  if i not in adds:
    adds.append(i)

print adds
'''
