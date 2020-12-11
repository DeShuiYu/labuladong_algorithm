'''
给定一个包含0，1，2，...，n中n个数的序列，找出0...n中没有出现在序列中的那个数。
'''

def missingNumber(nums):
    '''
    使用了异或运算的特性
    如果a、b两个值不相同，则异或结果为1。如果a、b两个值相同，异或结果为0。
    '''
    allnums = nums + [i for i in range(len(nums)+1)]
    res = 0
    for num in allnums:
        res ^= num
    return res

print(missingNumber([3,0,1])) # 2
print(missingNumber([9,6,4,2,3,5,7,0,1])) # 8