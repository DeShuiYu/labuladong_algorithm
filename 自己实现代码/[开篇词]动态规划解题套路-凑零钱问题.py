'''
给K种面值的硬币，面值分别为c1，c2,...,ck,每种硬币的数量无限，再给一个总金额amount，问你最少需要几枚硬币凑出这个金额，
如果不可能凑出，算法返回-1。
'''

def coinChange(coins:list,amount:int):
    def dp(n):
        if n == 0:
            return 0
        elif n < 0:
            return -1
        res = float('INF')
        for coin in coins:
            subproblem = dp(n-coin)
            if subproblem == -1:
                continue
            res = min(res,1+subproblem)
            return res
        return res if res != float('INF') else -1
    return dp(amount)

def _coinChange(coins:list,amount:int):
    '''
    加入备忘录
    '''
    memo = dict()
    def dp(n):
        if n in memo:
            return memo[n]
        if 0 == n :
            return 0
        if n < 0: 
            return -1
        res = float("INF")
        for coin in coins:
            subproblem = dp(n-coin)
            if subproblem == -1:continue
            res = min(res,1+ subproblem)
        memo[n] = res if res != float('INF') else -1
        return memo[n]
    return dp(amount)

def __coinChange(coins:list,amount:int):
    '''
    dp数组的迭代解法
    为啥dp数组初始化为amount+1尼，因为凑成amount金额的硬币数最多只可能等于amount(全用1元面值的硬币)，
    所以初始化为amount+1 就相当于初始化为正无穷，便于后续取最小值。
    '''
    dp = [amount + 1 for _ in range(amount+1)]
    dp[0] = 0
    for i in range(0,len(dp)):
        for coin in coins:
            if 0 > (i - coin):
                continue
            dp[i] = min(dp[i],1+dp[i-coin])
    return -1 if dp[amount] == amount+1 else dp[amount]