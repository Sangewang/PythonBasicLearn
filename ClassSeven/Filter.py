class Filter:
  
  def init(self):
    self.blocked = []

  def filter(self,sequence):
    return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
  def init(self):
    self.blocked = ['SPAM']

f = Filter()
f.init()
print f.filter([1,2,3])

s = SPAMFilter()
s.init()
print s.filter(['SPAM','SPAM','eggs','SPAM','bacon'])

print 'Judge SPAMFilter is Filter SubClass',issubclass(SPAMFilter,Filter)

print 'Get SPAMFilter SuperClass->',SPAMFilter.__bases__

print 'judge s is instance of SPAMFilter->',isinstance(s,SPAMFilter)
