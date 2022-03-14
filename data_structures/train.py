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

    def delete_node(self,key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        prev_node = None
        while cur_node and cur_node.data != key:
            prev_node = cur_node
            cur_node = cur_node.next
        if not cur_node:
            print('this node isn\'t in the list')
            return False
        prev_node.next = cur_node.next
        cur_node = None

    def delete_by_position(self, pos):
        if pos > len(self) or pos < 1:
            print("Your number out of list length ")
            return False
        cur_node = self.head
        if cur_node and pos == 1:
            self.head = cur_node.next
            cur_node = None
            return
        pos_node = 1
        prev_node = None
        while cur_node and pos != pos_node:
            prev_node = cur_node
            cur_node = cur_node.next
            pos_node += 1
        prev_node.next = cur_node.next
        cur_node = None



    def __len__(self):
        cur_node = self.head
        count = 0
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def swap_node(self,key_1, key_2):
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

        if not cur_2 or not  cur_1:
            return

        if prev_1:
            prev_1.next = cur_2
        else:
            self.head = cur_2

        if prev_2:
            prev_2.next = cur_1
        else:
            self.head = cur_1

        cur_1.next,cur_2.next = cur_2.next,cur_1.next


llist = LinkedList()
llist.add('A')
llist.add('B')
llist.add('C')
llist.add('D')
llist.add('E')
llist.add('F')
llist.swap_node("B","C")
# llist.delete_by_position(6)
# llist.delete_node("C")
# llist.prepend('R', "H")
# print(llist.is_include(llist.head,"A"))
llist.print_linked_list()