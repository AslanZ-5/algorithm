class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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


llist = CircularLinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
llist.prepend("E")
llist.print_list()
