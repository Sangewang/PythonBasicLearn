from functools import reduce

l = [1,2,3,4,5]
print(reduce(lambda x,y:x+y,l))
print(reduce(lambda x,y:x+y,l,10))


new_list = list(map(lambda x:x*2,l))
print(new_list)

merge_list = list(map(lambda x,y:x+y,l,new_list))
print(merge_list)

l = [100,80,60,40,20,0]
new = list(filter(lambda x:x<50,l))
print(new)
