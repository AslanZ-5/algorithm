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


def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == '}':
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    s = Stack()
    index = 0
    is_balanced = True
    while is_balanced is True and index < len(paren_string):
        paren = paren_string[index]
        if paren in '({[':
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1
    return is_balanced
  

a = '(())}'
print(is_paren_balanced(a))

# a = Stack()
# print(a.is_empty())
# a.push("A")
# a.push("B")
# a.push("C")
# a.push("D")
# print(a.pop())
# print(a.peek())
# print(a.get_stack())
