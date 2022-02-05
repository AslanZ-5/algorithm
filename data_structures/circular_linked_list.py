class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
            return
        new_node = Node(data)
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        cur.next = new_node
        new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def remove(self, data):
        if data == self.head.data:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev =cur
                cur = cur.next
                if cur.data == data:
                    prev.next = cur.next
                    cur = cur.next

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def split_list(self):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size // 2
        prev = None
        cur = self.head
        count = 0
        while cur and count < mid:
            prev = cur
            cur = cur.next
            count += 1
        prev.next = self.head

        splited_list = CircularLinkedList()
        while cur.next != self.head:
            splited_list.append(cur.data)
            cur = cur.next
        splited_list.append(cur.data)
        self.print_list()
        print("\n")
        splited_list.print_list()

    def remove_node(self, node):
        if node == self.head:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev =cur
                cur = cur.next
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next
    def josephus_circle(self,step):
        cur = self.head
        while len(self) > 1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1
            print('Removin: --',cur.data )
            self.remove_node(cur)
            cur = cur.next
    def is_circular_linked_list(self,input_list):
        cur = input_list.head
        while cur.next:
            cur = cur.next
            if cur.next == input_list.head:
                return True
        return False



llist = CircularLinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

llist1 = LinkedList()
llist1.append(0)
llist1.append(9)
llist1.append(8)
llist1.append(7)
# llist.josephus_circle(2)
# llist.split_list()
# llist.prepend("E")
# llist.remove("A")
llist.print_list()
print('-'*20)
llist1.print_list()
print('*'*20)
print(llist.is_circular_linked_list(llist))