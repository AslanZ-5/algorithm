class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def prepend(self, data):
        if not self.head:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = None
            self.head = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def append_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
            elif cur.data == key:
                nxt = cur.next
                new_node = Node(data)
                cur.next = new_node
                new_node.prev = cur
                new_node.next = nxt
                nxt.prev = new_node
            cur = cur.next

    def append_before_node(self,key,data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
            elif cur.data == key:
                new_node = Node(data)
                pr = cur.prev
                pr.next = new_node
                new_node.next = cur
                new_node.prev = pr
                cur.prev = new_node
            cur = cur.next





dllist = DoublyLinkedList()

dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append_before_node(1,99)
dllist.append_before_node(3,199)
dllist.print_list()
