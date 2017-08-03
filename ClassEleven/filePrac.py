f = open(r'somefile.txt','r')
print f.read(7)
print f.read(4)
f.close()

f = open(r'somefile.txt','r')
print f.read()
f.close()

f = open(r'somefile.txt','r')
for i in range(3):
  print str(i) + ': ' + f.readline()
f.close()


import pprint
pprint.pprint(open(r'somefile.txt').readlines())


f = open(r'somefile.txt','w')
f.write('this\nis no\nhaiku')
f.close()
f = open(r'somefile.txt')
print f.read()
f.close()

f = open(r'somefile.txt')
lines = f.readlines()
f.close()
lines[1] = "isn't a\n" 
f = open(r'somefile.txt','w')
f.writelines(lines)
f.close()

