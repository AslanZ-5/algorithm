class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data} -> {self.next}'

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print('Previous node is not in the list')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        'Deleting Node by his data value'
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_position(self, pos):
        "Deleteting node by given position"
        cur_node = self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        count = 1
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def len_iterative(self):
        """ Calculation length with iterative function"""
        cur_node = self.head
        count = 0
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self,node):
        """ Calculation length with recursive function"""
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)
    def swap_node(self,key_1,key_2):
        if key_1 == key_2:
            return
        prev_1 = None
        cur_1 = self.head
        while cur_1 and cur_1.data != key_1:
            prev_1 = cur_1
            cur_1 = cur_1.next
        prev_2 = None
        cur_2 = self.head
        while cur_2 and cur_2.data != key_2:
            prev_2 = cur_2
            cur_2 = cur_2.next
        if not cur_2 or not cur_1:
            return

        if prev_1:
            prev_1.next = cur_2
        else:
            self.head = cur_2
        if prev_2:
            prev_2.next = cur_1
        else:
            self.head = cur_1
        cur_1.next, cur_2.next = cur_2.next,cur_1.next

llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
# llist.prepend('E')
print(llist.len_iterative())
print(llist.len_recursive(llist.head))
# llist.insert_after_node(llist.head.next,"E")
llist.swap_node('B','C')

llist.print_list()
