## 用两个栈实现队列
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self, val):
        self.stack1.append(val)

    def pop(self):
        if not self.stack1 and not self.stack2:
            raise Exception("error:can't pop from empty queue!")
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
## test
sol = Solution()
sol.pop()
sol.push('a')
sol.push('b')
sol.push('c')
res = sol.pop()
res = sol.pop()
pass

## 用两个队列实现栈
class Solution:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    
    def push(self, val):
        if self.queue1 == []:
            self.queue2.append(val)
        elif self.queue2 == []:
            self.queue1.append(val)

    def pop(self):
        if not self.queue1 and not self.queue2:
            raise Exception("error:can't pop from empty stack!")
        
        if not self.queue2:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop()
        elif not self.queue1:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop()

## test
sol = Solution()
# sol.pop()
sol.push('a')
sol.push('b')
sol.push('c')
res = sol.pop()
res = sol.pop()
pass
