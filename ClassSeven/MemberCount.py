class MemberCounter:
  members = 0;

  def init(self):
    print 'init->', MemberCounter.members
    MemberCounter.members+=1

m1 = MemberCounter()
m1.init()
print m1.members

m2 = MemberCounter()
m2.init()
print m2.members

m1.members = 'Two'
m1.init()
print m1.members
