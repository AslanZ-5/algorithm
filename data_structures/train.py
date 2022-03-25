from linked_lists.linked_lists import LinkedList

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        cur_node = self.head
        while cur_node:

            print(cur_node.data)
            cur_node = cur_node.next
            if cur_node == self.head:
                break

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            return

        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        last_node.next = new_node
        new_node.next = self.head

    def prepend(self, node, data):
        if not self.is_include(node):
            print(f'Node "{node}" doesn\'t exist in the list')
            return False
        new_node = Node(data)
        if self.head.data == node:
            new_node = Node(data)
            new_node.next = self.head
            nxt = self.head
            self.head = new_node
            nxt.next = self.head

        cur_node = self.head
        prev_node = None
        while cur_node.next:
            prev_node = cur_node
            cur_node = cur_node.next
            if cur_node.data == node:
                prev_node.next = new_node
                new_node.next = cur_node

    def is_include(self, key):
        cur = self.head
        while cur:
            if key == cur.data:
                return True
        return False

    def remove(self, key):
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next

    def _remove_by_node(self, node):
        if self.head == node:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur == node:
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

    def split(self, key):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head

        n_list = CircularLinkedList()
        cur = self.head
        prev = None
        while cur.next != self.head:
            prev = cur
            cur = cur.next
            if cur.data == key:
                while cur:
                    n_list.add(cur.data)
                    cur = cur.next
                    if cur == self.head:
                        break
                prev.next = self.head
        print(self.print_linked_list())
        print('-------------------')
        print(n_list.print_linked_list())

    def split_into_two(self):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head
        mid = size // 2
        n_list = CircularLinkedList()
        cur = self.head
        c = 0
        prev = None
        while cur and c < mid:
            c += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        while cur.next != self.head:
            n_list.add(cur.data)
            cur = cur.next
        n_list.add(cur.data)

        print(self.print_linked_list())
        print('-------------------')
        print(n_list.print_linked_list())

    def josephus_problem(self,size):
        count = 1
        cur = self.head
        while cur.next != cur:
            if count == size:
                self._remove_by_node(cur)
                print(f'removed----{cur.data}')
                count = 0
            count += 1
            cur = cur.next
    def is_circular_llist(self,input_list):
        cur = input_list.head
        while cur:
            cur = cur.next
            if cur == input_list.head:
                return True
        return False



clist = CircularLinkedList()
llist = LinkedList()
llist.append(1)
llist.append(13)
llist.append(12)


clist.add('A')
clist.add('B')
clist.add('C')
clist.add('D')
# clist._remove_by_node(clist.head)
clist.print_linked_list()
print(clist.is_circular_llist(clist))
print(clist.is_circular_llist(llist))
# clist.josephus_problem(2)
# clist.print_linked_list()
# clist.split("C")
# clist.split_into_two()
# clist.remove('A')d
