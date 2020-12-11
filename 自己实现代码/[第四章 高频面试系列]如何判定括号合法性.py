
def isVaild(string:str)->bool:
    '''
    判断( 的情况
    '''
    left = 0
    for c in string:
        if c == "(":
            left +=1
        else:
            left -=1
        if left < 0:
            return False

    return left == 0

def _isVaild(string:str)->bool:
    left = []
    for c in string:
        if c == "(" or c == "{" or c == "[":
            left.append(c)
        else:
            if len(left) !=0  and leftOf(c) == left[-1]:
                left.pop()
            else:
                return False
    return len(left) == 0

def leftOf(c:str):
    if c == "}" :
        return "{"
    elif c == ")":
        return "("
    elif c == "]":
        return "["
    else:
        return ""
print(_isVaild("()[]{}")) # true
print(_isVaild("([)]")) # false
print(_isVaild("{[]}")) # true