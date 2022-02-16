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
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    else:
        return False


"""
User a stack to check whether or not a string 
has balanced usage of parenthesis.
Example: 
       (), ()(), (({[]}))  <- Balanced.
       ((), {{{)}], [][]]]] <- Not Balanced.
"""


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0
    while index < len(paren_string) and is_balanced:
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
    if s.is_empty() and is_balanced:
        return True
    else:
        return False


def div_by_2(dec_num):
    s = Stack()
    while dec_num:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num //= 2
    bin_num = ''
    while not s.is_empty():
        bin_num += str(s.pop())
    return bin_num
# print(div_by_2(22))


# Reverse string using python stack

def reverse_string(stack,input_str):
    # Loop through the string and push contents
    # character by character onto stack.
    for i in range(len(input_str)):
        stack.push(input_str[i])

    str_rev = ''
    while not stack.is_empty():
        str_rev += stack.pop()
    return str_rev
stack = Stack()
input_str = 'Hello'
print(reverse_string(stack,input_str))

