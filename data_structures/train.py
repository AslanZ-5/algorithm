class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        newnode = Node(data)
        cur = self.head
        prev = None
        while cur.next:
            cur = cur.next
        cur.next = newnode
        newnode.prev = cur

    def prepend(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append_after(self, key, data):
        if self.head is None:
            return "empty list"
        newnode = Node(data)
        cur = self.head
        while cur:
            if cur.data == key and cur.next is None:
                self.add(data)
                return
            elif cur.data == key and cur.next is not None:
                nxt = cur.next
                cur.next = newnode
                newnode.prev = cur
                newnode.next = nxt
                nxt.prev = newnode
            cur = cur.next

    def append_before(self, key, data):
        if self.head is None:
            return "empty list"
        newnode = Node(data)
        if self.head.data == key:
            self.prepend(data)
            return
        cur = self.head
        while cur.next:
            prev = cur
            cur = cur.next
            if cur.data == key:
                prev.next = newnode
                newnode.prev = prev
                newnode.next = cur
                cur.prev = newnode



dlist = DoublyLinkedList()
dlist.add("A")
dlist.add("B")
dlist.add("C")
dlist.add("D")

dlist.append_before("B","E")
dlist.print_list()
