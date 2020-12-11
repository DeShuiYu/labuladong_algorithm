def isPalindrome(s:str):
    return s == s[::-1]
def isPalindrome(nums:list):
    print(nums)
    print( nums[::-1])
    return nums == nums[::-1]

# print(isPalindrome([1,2,3]))