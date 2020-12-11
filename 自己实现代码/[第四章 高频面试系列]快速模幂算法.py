base = 1337

def mypow(a:int,b:int):
    a %= base

    res = 1
    for _ in range(b):
        res *= a
        res %= base

    return res

def superPow(a,b:list):
    if len(b) == 0 :
        return 1
    last = b.pop()
    part1 = mypow(a,last)
    part2 = mypow(superPow(a,b),10)

    return (part1 * part2) % base