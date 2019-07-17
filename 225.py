"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1); 
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false

"""

class MyStack:

    q1= []
    q2= []
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []
        
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.insert(0,x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.q1) > 1:
               self.q2.insert(0,self.q1.pop(-1))
        final = self.q1[0]
        self.q1 = self.q2
        self.q2 = []
        return final

    def top(self) -> int:
        """
        Get the top element.
        """
        while len(self.q1) > 0:
               if len(self.q1) == 1:
                       final = self.q1[0]
               self.q2.insert(0,self.q1.pop(-1))
               
        self.q1 = self.q2
        self.q2 = []
        return final
        
        