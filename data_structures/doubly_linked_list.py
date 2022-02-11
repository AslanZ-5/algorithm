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

    def append_before_node(self, key, data):
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

    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and self.head == cur:
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                else:
                    nxt = cur.next
                    nxt.prev = None
                    cur.next = None
                    cur = None
                    self.head = nxt
                    return
            elif cur.data == key:
                if not cur.next:
                    prev = cur.prev
                    cur.prev = None
                    prev.next = None
                    cur = None
                    return
                else:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def delete_node(self, node):
        cur = self.head
        while cur:
            if cur == node and self.head == cur:
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                else:
                    nxt = cur.next
                    nxt.prev = None
                    cur.next = None
                    cur = None
                    self.head = nxt
                    return
            elif cur == node:
                if not cur.next:
                    prev = cur.prev
                    cur.prev = None
                    prev.next = None
                    cur = None
                    return
                else:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def reverse_list(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp.prev:
            self.head = tmp.prev
    def remove_duplicates(self):
        cur = self.head
        d = dict()
        while cur:
            if cur.data in d:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt

            else:
                d[cur.data] = 1
                cur = cur.next
    def pairs_with_sum(self,sm):
        pairs = list()
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if p.data + q.data == sm:
                    pairs.append(f'({p.data},{q.data})')
                q = q.next
            p = p.next
        return pairs



dllist = DoublyLinkedList()

dllist.append(8)
dllist.append(4)
dllist.append(4)
dllist.append(6)
dllist.append(4)
dllist.append(8)
dllist.append(4)
dllist.append(10)
dllist.append(12)
dllist.append(12)
dllist.remove_duplicates()
print(dllist.pairs_with_sum(12))
dllist.print_list()
# print('---------',end='\n')
# dllist.reverse_list()
# dllist.print_list()