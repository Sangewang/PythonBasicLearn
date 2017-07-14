num = input("Please Enter a number :")
while num < 20:
  print num
  num+=1


name = ''
while not name or name.isspace():
  name = raw_input("Please Input a Name: ")
print 'Hello. %s!' % name
