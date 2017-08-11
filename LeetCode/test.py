
def longestCommonPrefix(strs):
    input = strs
    input.sort()
    str1 = input[0]
    str2 = input[-1]
    print(str1)
    common_len = 0
    if len(str1) <= len(str2):
      cnt = len(str1)
    else:
      cnt = len(str2)
    for i in xrange(cnt):
      if str1[i] == str2[i]:
        common_len = i+1
      else:
        break
    return str1[:common_len]

strs = [""]
print longestCommonPrefix(strs)


