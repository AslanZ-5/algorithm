class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, node, data):
        if not self.is_include(self.head,node):
            print(f'Node "{node}" doesn\'t exist in the list')
            return False
        new_node = Node(data)
        if self.head.data == node:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

        cur_node = self.head
        prev_node = None
        while cur_node.next:
            prev_node = cur_node
            cur_node = cur_node.next
            if cur_node.data == node:
                prev_node.next = new_node
                new_node.next = cur_node

    def append_to_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    def is_include(self,node,data):
        if not node:
            return False
        if node.data == data:
            return True
        return self.is_include(node.next, data)



llist = LinkedList()
llist.add('A')
llist.add('B')
llist.add('C')
llist.add('D')
llist.add('E')
llist.add('F')
llist.prepend('R', "H")
# print(llist.is_include(llist.head,"A"))
llist.print_linked_list()
