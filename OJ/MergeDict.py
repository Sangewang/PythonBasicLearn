def union_dict(dict1,dict2):
  out_dict = dict1.copy()
  for key2,value2 in dict2.items():
    value1 = out_dict.setdefault(key2,value2)
    if value1 != value2:
      out_dict[key2] = (value1,value2)

  return out_dict

dict1 = {'a':1,'b':2}
dict2 = {'a':1,'b':2}
print union_dict(dict1,dict2)

dict2 = {}
print union_dict(dict1,dict2)

dict2 = {'a':1,'b':3,'c':4}
print union_dict(dict1,dict2)

