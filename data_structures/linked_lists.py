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

    def len_recursive(self, node):
        """ Calculation length with recursive function"""
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_node(self, key_1, key_2):
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
        cur_1.next, cur_2.next = cur_2.next, cur_1.next

    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def merge_linked_list(self, llist):
        """ Merge Two Sorted Lists"""
        p = self.head
        q = llist.head
        s = None
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
        new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not q:
            s.next = p
        if not p:
            s.next = q
        return new_head

    def remove_duplicates(self):
        cur = self.head
        prev = None
        double_value = dict()

        while cur:
            if cur.data in double_value:
                # Remove Node
                prev.next = cur.next
                cur = None
            else:
                double_value[cur.data] = 1
                prev = cur
            cur = prev.next

    def print_nth_from_last(self, n):
        # Method 1
        total_len = self.len_iterative()
        cur = self.head
        while cur:
            if n == total_len:
                print(cur.data)
                return cur
            total_len -= 1
            cur = cur.next
        if cur is None:
            return

    def print_nth_from_last_method_2(self, n):
        p = self.head
        q = self.head
        count = 0
        while q and count < n:
            q = q.next
            count += 1
        if not q:
            print(str(n) + ' is greater than the number of nodes in list.')
            return
        while p and q:
            p = p.next
            q = q.next
        return p.data

    def count(self, item):
        cur = self.head
        count = 0
        while cur:
            if cur.data == item:
                count += 1
            cur = cur.next
        return count

    def count_recursive(self, item):
        def rec_count(cur, item):
            if not cur:
                return 0
            if cur.data == item:
                return 1 + rec_count(cur.next, item)
            else:
                return rec_count(cur.next, item)

        return rec_count(self.head, item)

    def rotate(self, k):
        p = self.head
        q = self.head
        prev = None
        count = 0
        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p = prev

        while q:
            prev = q
            q = q.next
        q = prev
        q.next = self.head
        self.head = p.next
        p.next = None

    def is_palindrome(self):
        s = ''
        p = self.head
        while p:
            s += str(p.data)
            p = p.next
        return s == s[::-1]

    def is_palindrome_method_2(self):
        p = self.head
        s = []
        while p:
            s.append(p.data)
            p = p.next
        p = self.head
        while p:
            data = s.pop()
            if data != p.data:
                return False
            p = p.next
        return True

    def is_palindrome_method_3(self):
        p = self.head
        q = self.head
        i = 0
        s = []
        while q:
            s.append(q)
            q = q.next
            i += 1
        q = s[i - 1]
        count = 1
        while count <= i // 2 + 1:
            if s[-count].data != p.data:
                return False
            p = p.next
            count += 1
        return True

    def move_tail(self):
        """Move Tail to Head"""
        last = self.head
        sec_to_last = None
        while last.next:
            sec_to_last = last
            last = last.next
        last.next = self.head
        sec_to_last.next = None
        self.head = last


llist = LinkedList()
# llist1 = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist.move_tail()
llist.print_list()
# print(llist.is_palindrome_method_3())
# print(llist.is_palindrome())
# print(llist.is_palindrome_method_2())
# print('////////////////////////')
# llist.rotate(4)
# llist.print_list()

# llist1.append(2)
# llist1.append(3)
# llist1.append(4)
# llist1.append(6)
# llist1.append(8)
# llist.prepend('E')
# print(llist.len_iterative())
# print(llist.len_recursive(llist.head))
# llist.insert_after_node(llist.head.next,"E")
# llist.swap_node('B','C')
# llist.reverse_iterative()
# llist.reverse_recursive()
# llist.merge_linked_list(llist1)
# llist.remove_duplicates()
# print(llist.print_nth_from_last_method_2(3))
# llist.print_list()
# print(llist.count_recursive('B'))
# print(llist.count('A'))
# print(llist.head)
