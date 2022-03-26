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


dlist = DoublyLinkedList()
dlist.add("A")
dlist.add("B")
dlist.add("C")
dlist.add("D")

dlist.prepend("E")
dlist.print_list()
