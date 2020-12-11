
# 如果返回[2,n)中的素数

def countPrimes(n:int):
    '''
    一般的代码可能是如下
    '''
    count = 0
    for i in range(2,n):
        if isPrime(i):
            count+=1
            print(i,end=" ")
    print()
    return count

def isPrime(n):
    from math import sqrt
    for i in range(2,int(sqrt(n))+1):
        if i * i > n:
            return False
        elif 0 == n % i:
            return False
    return True

def _countPrimes(n:int):
    '''
    高效的算法
    '''
    isPrim = [1 for _ in range(n+1)]
    isPrim[0],isPrim[1] = 0, 0
    i = 2
    while i * i <= n:
        if isPrime(i):
            j = i * i
            while j <= n:
                isPrim[j] = 0
                j+=i
        i+=1
    count = 0
    for i in range(len(isPrim)):
        if isPrim[i] == 1:
            count += 1
            print(i,end=" ")
    print()
    return count
            



print(countPrimes(10))
print(_countPrimes(10))


        