class FooBar:
  def __init__(self,value=42):
    self.somevar = value

f = FooBar()
print f.somevar

f = FooBar("Prace use __init__")
print f.somevar
