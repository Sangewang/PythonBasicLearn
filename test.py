def func(*arg_2,**arg_3):
  print(type(arg_2),arg_2)
  print(type(arg_3),arg_3)

func('Tom',1,2,3,china = 'Beijing',uk = 'London')
func('Tom',1,3)
