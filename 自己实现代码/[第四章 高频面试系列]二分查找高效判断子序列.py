def isSubsequence(s:str,t:str):
    """
    双向指针
    """
    i , j = 0 , 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i+=1
        j+=1

    return i == len(s)

def left_bound(arr,tar):
    lo ,hi = 0,len(arr)
    while lo < hi:
        mid = lo + (hi - lo )//2
        if tar > arr[mid]:
            lo = mid+1
        else:
            hi = mid
    return lo


def _isSubsequence(s:str,t:str):
    '''
    加入了二分查找算法
    '''
    m , n = len(s) , len(t)
    index = [[] for _ in range(256)]
    for i in range(n):
        index[ord(t[i])].append(i)

    j = 0
    for i in range(m):
        if len(index[ord(s[i])]) == 0:
            return False
        pos = left_bound(index[ord(s[i])],j)
        if pos ==  len(index[ord(s[i])]):
            return False
        j = index[ord(s[i])][pos]+1
    return True


if __name__ == "__main__":
    print(_isSubsequence("abc","ahbgdc"))
    print(_isSubsequence("axc","ahbgdc"))