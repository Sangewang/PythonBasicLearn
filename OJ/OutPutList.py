#!-*-coding:UTF-8 -*-

def flatten_list(in_list):
  if in_list is None:
    return None
  out_list = []
  len_list = len(in_list)
  for i in xrange(len_list):
    if not isinstance(in_list[i],list):
      out_list.append(in_list[i])
    else:
      out_list.extend(flatten_list(in_list[i]))
  return out_list

print flatten_list([1,[],2,[3,4,[5,6]],7,[8,9]])
print flatten_list([[],[[]]])
