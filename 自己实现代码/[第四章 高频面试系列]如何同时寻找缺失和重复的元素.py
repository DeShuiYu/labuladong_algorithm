def findErrorNums(nums:list):
    '''
    很巧，以下标的方式
    '''
    n = len(nums)
    dup = -1
    for i in range(n):
        index = abs(nums[i]) - 1
        if nums[index] < 0:
            dup = abs(nums[i])
        else:
            nums[index] *= -1
    missing = -1
    for i in range(n):
        if nums[i] > 0:
            missing = i+1
            break
    return [dup,missing]



print(findErrorNums([1,2,3,3,5]) )# [2,3]
# -1,-2,2,-4
# 2,