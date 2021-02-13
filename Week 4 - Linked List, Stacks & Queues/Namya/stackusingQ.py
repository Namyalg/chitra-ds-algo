#yep approach is the same for me as well

#maintain one to push in O(1)
#and another to pop out all elements except the last eleemtn and either pop or return it as top
#then push back all elements to the main stack

#Needs to be implemented using 2 queues

#Similarly, the push operation can be done in O(n) time by swapping on every addition
#and pop or top in O(1)

#add to the auxillary queue and get the contents from the actual queue and then add them all
#back to the actual queue so the top is at the bottom of the queue

#another approach is tht

'''
The element is added to the end of the queue
While the head of the queue is not equal to the element inserted, 
pop the element from the front and add it to the back of the queue


Eg : 1              =>   Q = >  1
     2                          1 , 2 
                                2, 1
    
    3                          2, 1, 3
                               1, 3, 2
                               3, 2, 1
                             
                             follows order and the min is at top of stack
                                    

'''
class MyStack:
    

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []
        self.top = -1

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.top += 1
        self.q1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.top == -1:
            return 
        elif self.top == 0:
            return(self.q1.pop(0))
        else:
            tp = self.top
            while tp != 0:
                self.q2.append(self.q1.pop(0))
                tp -= 1 
            temp = self.q1.pop(0)
            self.top -= 1
            while len(self.q2) != 0:
                self.q1.append(self.q2.pop(0))
        return temp

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.top == -1:
            return 
        elif self.top == 0:
            return(self.q1[self.top])
        else:
            tp = self.top
            while tp != 0:
                self.q2.append(self.q1.pop(0))
                tp -= 1 
            temp = self.q1[self.top]
            while len(self.q2) != 0:
                self.q1.append(self.q2.pop(0))
        return temp
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) >= 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
