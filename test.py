def twoSum( nums, target):
    result = []
    count = len(nums)
    for i in range(0,count):
        for j in range(i+1,count):
            if nums[i]+nums[j] == target:
               print i
               print j
               print nums[i]
               print nums[j]
               result.append(i)
               result.append(j)
               break
    return result



num = [3,2,4]
target = 6
print twoSum(num,target)
