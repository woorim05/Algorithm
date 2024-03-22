class Stack:
    def __init__(self):
        self.items = []
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return -1
     
    def push(self, item):
        self.items.append(item)
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        if len(self.items) == 0:
            return 1
        else: 
            return 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return -1

import sys
n = int(sys.stdin.readline().strip())
stack = Stack()
result = []
for i in range(n):
    k = sys.stdin.readline().strip()
    if k == "2": print(stack.pop())
    elif k == "3": print(stack.size())
    elif k == "4": print(stack.is_empty())
    elif k == "5": print(stack.peek())
    else: stack.push(int(k.split()[1]))