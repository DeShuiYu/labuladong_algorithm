'''
先自己使用动态规划做做
'''
'''
    给定一个非负整数数组，你最初位于数组的第一个位置
    数组中的每个元素代表你在该位置可以跳跃的最大长度
    判断你是否能够达到最后一个位置
'''
def canJump(nums:list):
    '''
    贪心算法：考虑最大能达到的位置
    '''
    n = len(nums)
    farthest = 0
    for i in range(n-1):
        # 不断计算能跳到的最远距离
        farthest = max(farthest,i+nums[i])
        # 卡住了
        if farthest <= i:
            return False
    return farthest >= n-1


'''
[2,3,1,1,4] --> True
[3,2,1,0,4] --> False
'''

# print(canJump([2,3,1,1,4]))
# print(canJump([3,2,1,0,4]))



'''
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
'''
from typing import List
memo = None
def jump(nums:List[int]):
    '''
    动态规划
    '''
    global memo
    n = len(nums)
    memo = [n for _ in range(n)]
    return dp(nums,0) # 从索引0 跳到最后一步至少需要的步数

def dp(nums:List[int],p:int):
    '''
    定义索引p跳到最后最后一格，至少需要dp(nums,p)步
    '''
    n = len(nums)
    if p >= n-1:#已经到达最后了不需要跳了
        return 0
    if memo[p] != n:
        return memo[p]
    steps = nums[p]

    # 你可以选择跳1步，2步...
    for i in range(1,steps+1):# 1,2,3,...,steps
        subProblem = dp(nums,p+i) # 子问题的最小步数
        memo[p] = min(memo[p],subProblem + 1)
    return memo[p]


# print(jump([2,3,1,1,4])) # 2


def _jump(nums:list):
    n = len(nums)
    jumps,end,farthest = 0,0 , 0
    for i in range(n-1):
        farthest = max(nums[i] + i ,farthest)
        if i == end:
            jumps +=1
            end = farthest

    return jumps
print(_jump([2,3,1,1,4])) # 2
