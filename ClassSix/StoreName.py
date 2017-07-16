def init(data):
  data['first']  = {}
  data['middle'] = {}
  data['last']   = {}

def lookup(data,label,name):
 #print 'lookup -> data[label]',data[label]
  return data[label].get(name)

def store(data,full_name):
  names = full_name.split()
  #print 'full_name=',full_name
  #print 'names=',names
  if len(names) == 2:names.insert(1,'')
  labels = 'first','middle','last'
  for label,name in zip(labels,names):
   #print 'label=',label,'name=',name
    people = lookup(data,label,name)
   #print people
    if people:  
      people.append(full_name)
    else:
      data[label][name] = [full_name]

MyNames = {}
init(MyNames)
store(MyNames,'Magnus Lie Hetland')
print lookup(MyNames,'middle','Lie')

