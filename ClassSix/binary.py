def search(sequence,number,lower,upper):
  if lower == upper:
    assert number==sequence[upper],'Can not Find The Target'
    return upper
  else:
    middle = (lower+upper)//2
    if number>sequence[middle]:
      return search(sequence,number,middle+1,upper)
    else:
      return search(sequence,number,lower,middle)

seq = [34,67,8,123,4,100,95]
print 'seq =',seq
seq.sort()
print 'After seq sort =',seq
print 'The length of seq =',len(seq)
print search(seq,95,0,len(seq))
