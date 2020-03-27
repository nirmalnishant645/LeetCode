'''
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
'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
        

    def push(self, x: int) -> None:
        '''
        Time Complexity: O(1)
        Space Complecity: O(1)
        '''
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        

    def pop(self) -> None:
        '''
        Time Complexity: O(1)
        Space Complecity: O(1)
        '''
        n = self.stack.pop()
        if self.min_stack[-1] == n:
            self.min_stack.pop()
        return n
        

    def top(self) -> int:
        '''
        Time Complexity: O(1)
        Space Complecity: O(1)
        '''
        return self.stack[-1]
        

    def getMin(self) -> int:
        '''
        Time Complexity: O(1)
        Space Complecity: O(1)
        '''
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
