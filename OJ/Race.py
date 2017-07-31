def race(horseNum,horseQi,horseTian):
  maxWinNumTian = 0
  horseQi_S = sorted(horseQi)
  horseTian_S = sorted(horseTian)
  for i in xrange(horseNum):
    for j in horseTian_S:
      if j > horseQi_S[i]:
        maxWinNumTian+=1
        horseTian_S.remove(j)
        break
  return maxWinNumTian

horseQi = [1,2,4]
horseTian = [9,3,2]
horseNum = len(horseQi)
print race(horseNum,horseQi,horseTian)

horseQi = [1,2,3]
horseTian = [3,2,1]
horseNum = len(horseQi)
print race(horseNum,horseQi,horseTian)

horseQi = [1]
horseTian = [1]
horseNum = len(horseQi)
print race(horseNum,horseQi,horseTian)

horseQi = [1,2,3]
horseTian = [9,3,1]
horseNum = len(horseQi)
print race(horseNum,horseQi,horseTian)

horseQi = [1,2,3,4,5,6,7,8,9]
horseTian = [1,2,3,4,5,6,7,8,9]
horseNum = len(horseQi)
print race(horseNum,horseQi,horseTian)
