class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, element):
        self.queue.append(element)
    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty'
        return self.queue.pop(0)
    def peek(self):
        if self.isEmpty():
            return 'Queue is empty'
        return self.queue[0]
    def isEmpty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)
    

# myQueue = Queue()
# myQueue.enqueue('A')
# myQueue.enqueue('B')
# myQueue.enqueue('C')
# print('Queue: ', myQueue.queue)
# print('Dequeue: ', myQueue.dequeue)
# print('Peek: ', myQueue.peek)
# print('isEmpty: ', myQueue.enqueue)
# print('Size: ', myQueue.size)


class Stack:
    def __init__(self):
        self.stack = []
    def push(self, element):
        self.stack.append(element)
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return 'Stack is empty'
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
    

# myStack = Stack()

# myStack.push('A')
# myStack.push('B')
# myStack.push('C')
# print('Stack: ', myStack.stack)

# print('Pop: ', myStack.pop())

# print('Peek: ', myStack.peek())

# print('isEmpty: ', myStack.isEmpty())

# print('Size: ', myStack.size())

x = lambda x, y: x + y
print(x(5, 6))
