f = open(r'\var\www\Python\ClassEleven\somefile.txt','w')
f.write('0123467890123456789')
f.seek(5)
print f.tell()
f.write('Hello World!')
f.close()

f = open(r'\var\www\Python\ClassEleven\somefile.txt','r')
print f.read()
