# https://leetcode.com/problems/implement-queue-using-stacks/description/
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.enqueue = []
        self.dequeue = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.enqueue.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.dequeue) == 0:
            while len(self.enqueue) > 0:
                self.dequeue.append(self.enqueue.pop())
        return self.dequeue.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.dequeue) == 0:
            while len(self.enqueue) > 0:
                self.dequeue.append(self.enqueue.pop())
        return self.dequeue[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.dequeue) == 0 and len(self.enqueue) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()