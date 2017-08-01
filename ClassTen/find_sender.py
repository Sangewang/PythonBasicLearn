import fileinput,re
pat = re.compile('From: (.*) <.*?>$')
for line in fileinput.input():
  m = pat.match(line)
  if m:
    print m.group(0)
    print m.group(1)


pat = re.compile(r'[a-z\-\.]+@[a-z\-\.]+',re.IGNORECASE)
addresses =  set()
for line in fileinput.input():
  for address in pat.findall(line):
    addresses.add(address)

for address in sorted(list(addresses)):
  print address

'''
adds = []
for i in addresses:
  if i not in adds:
    adds.append(i)

print adds
'''
