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

    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # Case1
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                # Case 2
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return
            elif cur.data == key:
                # Case 3
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                # Case 4
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def delete_node(self, node):
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                # Case1
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                # Case 2
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return
            elif cur == node:
                # Case 3
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                # Case 4
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev

    def remove_duplicates(self):
        dn = dict()
        cur = self.head
        while cur:
            if cur.data in dn:
                self.delete_node(cur)
            else:
                dn[cur.data] = 1
            cur = cur.next
    def pairs_with_sum(self, sum_val):
        pairs = list()
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if q.data + p.data == sum_val:
                    pairs.append(f'({p.data},{q.data})')
                q = q.next
            p = p.next
        return pairs
    def __len__(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count


dlist = DoublyLinkedList()
dlist.add(1)
dlist.add(2)
dlist.add(3)
dlist.add(4)
dlist.add(5)
print(dlist.pairs_with_sum(5))
# dlist.delete("C")
dlist.remove_duplicates()
# dlist.reverse()
# dlist.append_before("B","E")
dlist.print_list()
