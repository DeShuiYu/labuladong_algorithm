def minEatingSpeed(piles:list,H:int):
    '''
    吃香蕉问题
    '''
    maxSpeed = max(piles)
    for speed in range(1,maxSpeed):
        if canFinish(piles,speed,H):
            return speed

    return maxSpeed

def canFinish(piles:list,speed:int,H:int):
    time = 0
    for n in piles:
        time += timeOf(n,speed)
    return time <= H

def timeOf(n:int,speed:int):
    return (n//speed) + (1 if n % speed > 0 else 0)

# print(minEatingSpeed([3,6,7,11],8)) # 4
# print(minEatingSpeed([30,11,23,4,20],5))# 30


def shipWithinDays(weights:list,D:int):
    for weight in range(max(weights),sum(weights)):
        if canshipWithinDays(weights,D,weight):
            return weight
    return sum(weights)

def canshipWithinDays(weights,D,weight):
    i = 0
    for day in range(D):
        maxCap = weight
        while True:
            maxCap -= weights[i]
            if maxCap < 0:
                break
            i+=1
            if i == len(weights):
                return True
        
    return False

print(shipWithinDays([1,2,3,4,5,6,7,8,9,10],5)) # 15
