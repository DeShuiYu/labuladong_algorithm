
class MinStack:
    def __init__(self):
        self.mainStack = []
        self.minStack = []

    def push(self,ele:int):
        '''
        压栈
        '''
        self.mainStack.append(ele)
        if len(self.minStack) == 0  or ele < self.minStack[-1]:
            self.minStack.append(ele)

    def pop(self):
        ''' 
        出栈并返回数据
        '''
        ele = self.mainStack.pop()
        if ele == self.minStack[-1]:
            self.minStack.pop()
        return ele

    def getMin(self):
        '''
        得到栈中最小值
        '''
        return self.minStack[-1]

if __name__ == "__main__":
    stack = MinStack()
    stack.push(4)
    stack.push(9)
    stack.push(7)
    stack.push(3)
    stack.push(8)
    stack.push(5)
    print(stack.getMin()) # 3
    print("-"*30)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print("-"* 30)
    print(stack.getMin()) # 4