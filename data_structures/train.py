class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def get_stack(self):
        return self.items


a = Stack()
print(a.is_empty())
a.push("A")
a.push("B")
a.push("C")
a.push("D")
print(a.pop())
print(a.peek())
print(a.get_stack())
