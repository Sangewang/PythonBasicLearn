num = input('Enter a number :')
if num>0 :
  print 'The number is positive'
elif num<0 :
  print 'The number is negative'
else:
  print 'The number is zero'



name = raw_input('What is your name? ')
if name.endswith('Gumby'):
  if name.startswith('Mr.'):
    print 'Hello, Mr Gumby'
  elif name.startswith('Mrs.'):
    print 'Hello, Mrs Gumby'
  else:
    print 'Hello,Gumby'
else:
  print 'Hello Stranger'
