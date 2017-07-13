database=[
  ['albert','1234'],
  ['dilbert','4234'],
  ['smith','7524'],
  ['jones','9843']
]

user = raw_input('User name: ')
pin  = raw_input('PIN code: ')

if [user,pin] in database : print 'Access granted'
