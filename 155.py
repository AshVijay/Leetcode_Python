"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
  

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.


"""        
class MinStack:
    list_s = []
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list_s = []

    def push(self, x: int) -> None:
        self.list_s.append(x)
              

    def pop(self) -> None:
        if len(self.list_s) == 0 :
              return -1
        self.list_s.pop(-1)
        

    def top(self) -> int:
        return self.list_s[-1]

    def getMin(self) -> int:
        return min(self.list_s)

        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()