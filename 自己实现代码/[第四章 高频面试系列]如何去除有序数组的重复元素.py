def my(nums:list):
    return len(set(nums))


def removeDuplicates(nums:list):
    '''
    这个是书上的算法，但是如果测试数据用[1,2,1] 得到 3
    如果测试数据用[1,1,2]得到 2
    因此，此算法还是慎重选择。
    '''
    n = len(nums)
    if 0 == n : 
        return 0
    slow ,fast = 0,1
    while fast < n:
        if nums[fast] != nums[slow]:
            slow+=1
            nums[slow] = nums[fast]
        fast+=1
    return slow+1

print(my([1,2,1]))
print(removeDuplicates([1,2,1]))
    