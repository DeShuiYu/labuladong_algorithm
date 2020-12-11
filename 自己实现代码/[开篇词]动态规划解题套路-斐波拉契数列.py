def fib(N:int):
    '''
    带备忘录的斐波拉契数列
    '''
    if N < 1:
        return 0
    memo = [0 for _ in range(N+1)]
    return helper(memo,N)

def helper(memo,N:int):
    if N == 1 or N==2:
        return 1
    if memo[N] != 0:
        return memo[N]
    return helper(memo,N-1)+helper(memo,N-2)

def _fib(N:int)->int:
    '''
    dp 数组的迭代解法
    '''
    dp = [0 for _ in range(N+1)]
    dp[1],dp[2] = 1,1
    for i in range(3,N+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[N]

def __fib(N:int)->int:
    if 1 == N or 2 == N:
        return 1  
    prev,curr = 1,1
    for i in range(3,N+1):
        sum = prev + curr
        prev = curr
        curr = sum
    return curr

# print(__fib(5))