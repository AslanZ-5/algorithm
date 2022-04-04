from stacks.the_stack import Stack


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Queue(object):
    def __init__(self, ):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(tree.root, "")
        if traversal_type == 'inorder':
            return self.print_inorder(tree.root, "")
        if traversal_type == 'postorder':
            return self.print_postorder(tree.root, "")
        if traversal_type == 'levelorder':
            return self.levelorder_print(tree.root)
        else:
            print(f"Travelsal type unsupported")

    def preorder_print(self, start, traversal):
        """Root => Left => Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def print_inorder(self, start, traversal):
        if start:
            traversal = self.print_inorder(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.print_inorder(start.right, traversal)
        return traversal

    def print_postorder(self, start, traversal):
        if start:
            traversal = self.print_inorder(start.left, traversal)
            traversal = self.print_inorder(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def levelorder_print(self, start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ''
        while len(queue) > 0:
            traversal += str(queue.peek()) + '-'
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def height_node(self, node):
        if node is None:
            return -1
        left_height = self.height_node(node.left)
        right_height = self.height_node(node.right)
        return 1 + max(left_height, right_height)

    def reverse_levelorder_print(self, start):
        if start is None:
            return
        n_queue = Queue()
        stack = Stack()
        n_queue.enqueue(start)
        while len(n_queue) > 0:
            node = n_queue.dequeue()
            stack.push(node.value)
            if node.left:
                n_queue.enqueue(node.left)
            if node.right:
                n_queue.enqueue(node.right)
        a = ''
        while not stack.is_empty():
            a += str(stack.pop()) + '-'
        return a



tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print(tree.reverse_levelorder_print(tree.root))
print(tree.height_node(tree.root))
print('preorder', tree.print_tree('preorder'))
print('inorder', tree.print_tree('inorder'))
print('postorder', tree.print_tree('postorder'))
print('levelorder', tree.print_tree('levelorder'))
