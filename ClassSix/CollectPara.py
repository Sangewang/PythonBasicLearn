def print_params(title,*pa,**params):
  print title
  print pa
  print params

print_params('This','a','test',some=6)
print_params('Nothing:',somthing=42)
