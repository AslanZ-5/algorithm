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
        if not self.is_include(self.head, node):
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

    def is_include(self, node, data):
        if not node:
            return False
        if node.data == data:
            return True
        return self.is_include(node.next, data)

    def delete_node(self, key):
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

    def reverse_node(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def reverse_rec(self):
        def _reverse_rec(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_rec(cur, prev)

        self.head = _reverse_rec(cur=self.head, prev=None)

    def merge_list(self, llist):
        p = self.head
        q = llist.head
        s = None
        if not p:
            return q
        if not q:
            return p
        if p.data <= q.data:
            s = p
            p = s.next
        else:
            s = q
            q = s.next
        self.head = s
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

    def remove_duplicates(self):
        d = dict()
        cur = self.head
        prev = None
        while cur:
            if cur.data in d:
                prev.next = cur.next
                cur = None
            else:
                d[cur.data] = 1
                prev = cur
            cur = prev.next

    def print_nth_from_last(self, n):
        total_len = len(self)
        cur = self.head
        while cur:
            if total_len == n:
                return cur.data
            total_len -= 1
            cur = cur.next

    def print_nth_from_last_2(self, n):
        p = self.head
        q = self.head
        count = 0
        while q and count < n:
            q = q.next
            count += 1
        if not q:
            print(f'{n} is greater than the number of nodes in list')

        while p and q:
            p = p.next
            q = q.next
        return p.data

    def count_occurences_1(self, key):
        cur = self.head
        count = 0
        while cur:
            if key == cur.data:
                count += 1
            cur = cur.next
        return count

    def count_occ_rec(self, node, key):
        if not node.next:
            return 0
        if key == node.data:
            return 1 + self.count_occ_rec(node.next, key)
        else:
            return  self.count_occ_rec(node.next, key)

    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head

        sum_list = LinkedList()

        carry = 0

        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry

            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_list.add(remainder)
            else:
                carry = 0
                sum_list.add(s)
            if p:
                p = p.next
            if q:
                q = q.next
        sum_list.print_linked_list()

    def rotate(self, key):
        cur = self.head
        k = 1
        k_node = None
        while cur.next:
            if key == k:
                k_node = cur
            cur = cur.next
            k += 1
        if not k_node:
            return 'Something wrong'
        cur.next = self.head
        self.head = k_node.next
        k_node.next = None

    def is_palindrom_1(self):
        cur = self.head
        st = ''
        while cur:
            st += str(cur.data)
            cur = cur.next
        return st == st[::-1]

    def is_palindrom_2(self):
        cur = self.head
        ls = []
        while cur:
            ls.append(cur.data)
            cur = cur.next
        cur = self.head
        while cur:
            if cur.data != ls.pop():
                return False
            cur = cur.next
        return True

    def is_palindrom_3(self):
        p = self.head
        q = self.head
        ls = []
        i = 0
        while q:
            ls.append(q)
            i += 1
            q = q.next
        q = ls[i - 1]

        count = 1
        while count <= i//2 +1:
            if ls[-count].data != p.data:
                return False
            p = p.next
            count += 1
        return True

    def move_tail_to_head(self):
        cur = self.head
        prev = None
        while cur.next:
            prev = cur
            cur = cur.next
        cur.next = self.head
        self.head = cur
        prev.next = None


    # llist = LinkedList()


# llist.add('A')
# llist.add('B')
# llist.add('C')
# llist.add('D')
# llist.add('E')
# llist.add('F')
# llist.reverse_rec()
# llist.reverse_node()
# llist.swap_node("B","C")
# llist.delete_by_position(6)
# llist.delete_node("C")
# llist.prepend('R', "H")
# print(llist.is_include(llist.head,"A"))

llist1 = LinkedList()
llist2 = LinkedList()


llist1.add(7)
llist1.add(9)
llist1.add(10)
# llist1.rotate(4)
llist1.add(5)
llist1.add(6)
llist1.add(5)
# print(llist1.is_palindrom_1())
# print(llist1.is_palindrom_2())
# print(llist1.is_palindrom_3())
llist1.move_tail_to_head()

# print('count --- ', llist1.count_occurences_1(7))
# print('count recursevly --- ', llist1.count_occ_rec(llist1.head,7))

# llist2.add(8)
# llist2.add(4)
# llist2.add(2)
# llist2.add(6)
# llist2.add(8)
# llist1.merge_list(llist2)
# llist1.sum_two_lists(llist2)
# print(llist1.print_nth_from_last(2))
# print(llist1.print_nth_from_last_2(2))
# llist1.remove_duplicates()
llist1.print_linked_list()
