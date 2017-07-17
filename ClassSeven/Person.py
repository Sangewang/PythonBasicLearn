class Person:

  def setName(self,name):
    self.name = name

  def getName(self):
    return self.name

  def greet(self):
    print "Hello, World! I'm %s."% self.name

 
foo = Person()
foo.setName('Luke Skywalker')
foo.greet()

bar = Person()
bar.setName('Anak in Skywalker')
bar.greet()
