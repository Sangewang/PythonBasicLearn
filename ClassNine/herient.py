class A:
  def hello(self):
    print "I'm A"

class B(A):
  def hello(self):
    print "I'm B"


a = A()
a.hello()

b = B()
b.hello()


