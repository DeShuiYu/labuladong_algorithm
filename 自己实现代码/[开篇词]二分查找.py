from typing import List
def binarySearch(nums:list,target:int):
    '''
    二分查找算法
    注意mid+1和mid-1，否则可能会陷入无限循环
    '''
    left,right = 0,len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid+1 
        elif nums[mid] > target:
            right = mid-1
        elif nums[mid] == target:
            return mid
    return -1

def left_bound(nums:List[int],target:int):
    '''
    寻找左侧边界的二分搜索
    '''
    if len(nums) == 0:
        return -1
    left,right = 0,len(nums)-1
    while left < right:
        mid = (left + right ) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1

    return left 

def right_bound(nums:List[int],target:int):
    '''
    寻找右侧边界的二分搜索
    '''
    if len(nums) == 0:
        return -1
    left,right = 0,len(nums)-1
    while left < right:
        mid = (left + right ) // 2
        if nums[mid] == target:
            left = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1

    return right    

print(binarySearch([1,2,2,2,5,6],2))
print(left_bound([1,2,2,2,5,6],2))
print(right_bound([1,2,2,2,5,6],2))